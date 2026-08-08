#!/usr/bin/env python3
"""PreToolUse gate for the Assignment OS pipeline.

Enforces the rules that CLAUDE.md calls non-negotiable, in code rather than prose:
  1. formatter never runs unless check_report.json verdict == "PASS"
  2. strict-checker never runs a 3rd loop (loop_count >= 2 -> surface HITL instead)
  3. research-planner never runs while the Evidence Contract is unresolved -- research built on
     unseen artifacts is the failure mode that produced a 0.4-confidence load-bearing assumption

Override: set "gate_override": "<reason>" in the active assignment's state.json. Non-empty lets
the call through and says so loudly. Deliberate by construction: you must open the file and write
a reason, so it can't be tripped by accident mid-run.

Silence == allow. Only denials produce output, so normal permission flow is untouched otherwise.
Runs on every Task call, so it fails open on anything unexpected: a gate that crashes the
pipeline on malformed input is worse than one that misses an edge case.
"""
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATED = ("formatter", "strict-checker", "research-planner")
DONE = ("complete",)


def deny(reason):
    json.dump({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }}, sys.stdout)
    sys.exit(0)


def allow():
    sys.exit(0)


def load_json(path):
    try:
        return json.load(open(path))
    except Exception:
        return {}


def read_int(d, key):
    try:
        return int((d or {}).get(key) or 0)
    except (TypeError, ValueError):
        return 0


def active_assignment(state_paths):
    """Newest *unfinished* assignment -> (dir, state). Plain mtime would pick a `complete`
    assignment the moment /debrief touches its state.json, gating the live run against the
    wrong folder's check_report.json. Returns None if nothing is readable."""
    candidates = []
    for p in state_paths:
        try:
            state = json.load(open(p))
        except Exception:
            continue
        if str(state.get("status") or "").lower() in DONE:
            continue
        candidates.append((os.path.getmtime(p), os.path.dirname(p), state))
    if not candidates:
        return None
    _, adir, state = max(candidates, key=lambda c: c[0])
    return adir, state


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        allow()

    agent = (payload.get("tool_input") or {}).get("subagent_type") or ""
    if agent not in GATED:
        allow()

    found = active_assignment(glob.glob(os.path.join(ROOT, "Companies", "*", "*", "state.json")))
    if not found:
        allow()
    adir, state = found

    override = str(state.get("gate_override") or "").strip()
    if override:
        allow()

    if agent == "formatter":
        report = os.path.join(adir, "check_report.json")
        if not os.path.exists(report):
            deny("Formatter blocked: no check_report.json in %s. Run strict-checker first."
                 % os.path.basename(adir))
        try:
            verdict = str(json.load(open(report)).get("verdict") or "").upper()
        except Exception:
            deny("Formatter blocked: check_report.json is unreadable. Re-run strict-checker.")
        if verdict != "PASS":
            deny('Formatter blocked: Checker verdict is "%s", not PASS. Fix the draft and re-run '
                 'strict-checker. To bypass deliberately, set "gate_override": "<reason>" in '
                 'state.json.' % (verdict or "missing"))

    if agent == "research-planner":
        contract = os.path.join(adir, "workspace", "evidence_contract.md")
        # Absent contract -> legacy assignment predating this gate. Fail open, don't strand it.
        if os.path.exists(contract):
            status = str((state.get("evidence_contract") or {}).get("status") or "").lower()
            if status != "resolved":
                deny('Research blocked: workspace/evidence_contract.md is unresolved. Every row '
                     'must be supplied or waived (waived rows carry their consequence into the '
                     'deliverable\'s assumptions). Run /intent-confirm, then set '
                     '"evidence_contract": {"status": "resolved"} in state.json. To bypass '
                     'deliberately, set "gate_override": "<reason>" in state.json.')

    if agent == "strict-checker":
        # Two counters existed and nothing kept them in sync: state.loop_count (hand-edited,
        # so in practice never incremented) and check_report.loop_number (written by the
        # checker itself every run). Trust the higher one -- the cap then holds on the
        # checker's own evidence instead of on a counter no code writes.
        loops = max(read_int(state, "loop_count"),
                    read_int(load_json(os.path.join(adir, "check_report.json")), "loop_number"))
        if loops >= 2:
            deny('Loop cap hit: strict-checker has already failed %d times. Surface the best draft '
                 'and the unmet criteria to the user instead of a third auto-loop. To bypass '
                 'deliberately, set "gate_override": "<reason>" in state.json.' % loops)

    allow()


def selftest():
    """python3 gate_check.py --selftest — asserts the assignment picker, the part most likely to
    break silently (a wrong pick gates the right agent against the wrong folder's artifacts)."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        def mk(name, status, mtime):
            d = os.path.join(tmp, name)
            os.makedirs(d)
            p = os.path.join(d, "state.json")
            json.dump({"status": status}, open(p, "w"))
            os.utime(p, (mtime, mtime))
            return p

        live = mk("live", "active", 1000)
        debriefed = mk("debriefed", "complete", 9000)   # newest by mtime, but finished
        # The regression this guards: /debrief touches a completed assignment, whose state.json
        # then wins on mtime alone and gates the live run against the wrong check_report.json.
        adir, state = active_assignment([live, debriefed])
        assert os.path.basename(adir) == "live", adir
        assert state["status"] == "active"
        # Nothing unfinished -> caller falls through to allow(), never gates on a stale folder.
        assert active_assignment([debriefed]) is None
        # Unreadable state.json is skipped, not fatal (hook must fail open).
        bad = os.path.join(tmp, "bad_state.json")
        open(bad, "w").write("{not json")
        assert os.path.basename(active_assignment([bad, live])[0]) == "live"

        # Loop cap reads whichever counter is higher. The regression this guards: state.json's
        # loop_count is hand-maintained and in practice stays 0, so trusting it alone let the
        # checker loop forever. check_report.loop_number is written by the checker every run.
        assert max(read_int({"loop_count": 0}, "loop_count"),
                   read_int({"loop_number": 2}, "loop_number")) == 2
        assert read_int({}, "loop_count") == 0            # missing key -> 0, not a crash
        assert read_int({"loop_count": "oops"}, "loop_count") == 0   # garbage -> 0
        assert load_json("/nonexistent/x.json") == {}     # absent report -> {}, fail open
    print("gate_check selftest: ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        main()
