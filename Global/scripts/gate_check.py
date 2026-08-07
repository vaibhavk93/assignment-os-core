#!/usr/bin/env python3
"""PreToolUse gate for the Assignment OS pipeline.

Enforces the two rules that CLAUDE.md calls non-negotiable, in code rather than prose:
  1. formatter never runs unless check_report.json verdict == "PASS"
  2. strict-checker never runs a 3rd loop (loop_count >= 2 -> surface HITL instead)

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
GATED = ("formatter", "strict-checker")


def deny(reason):
    json.dump({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }}, sys.stdout)
    sys.exit(0)


def allow():
    sys.exit(0)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        allow()

    agent = (payload.get("tool_input") or {}).get("subagent_type") or ""
    if agent not in GATED:
        allow()

    states = glob.glob(os.path.join(ROOT, "Companies", "*", "*", "state.json"))
    if not states:
        allow()

    state_path = max(states, key=os.path.getmtime)
    adir = os.path.dirname(state_path)
    try:
        state = json.load(open(state_path))
    except Exception:
        allow()

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

    if agent == "strict-checker":
        try:
            loops = int(state.get("loop_count") or 0)
        except (TypeError, ValueError):
            loops = 0
        if loops >= 2:
            deny('Loop cap hit: strict-checker has already failed %d times. Surface the best draft '
                 'and the unmet criteria to the user instead of a third auto-loop. To bypass '
                 'deliberately, set "gate_override": "<reason>" in state.json.' % loops)

    allow()


if __name__ == "__main__":
    main()
