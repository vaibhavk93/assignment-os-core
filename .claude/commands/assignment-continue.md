---
description: Resume a paused or failed assignment from its last checkpoint, or rewind it to an earlier stage.
---

`$ARGUMENTS` is optional and may be an assignment path, a stage name, or both.

1. Find the most recently modified `state.json` under `Companies/**` with `status` in `active`/`paused`/`failed` (or use the assignment path from `$ARGUMENTS` if given). This mirrors `gate_check.py`, which ignores `status: complete` — a `/debrief`-ed old assignment must never hijack a live run.
2. Read it, plus `Companies/<Company>/Company_Memory.md` and `workspace/intent.md`.
3. Report to the user: current stage, what's pending, loop count, any open questions.
4. **If `$ARGUMENTS` names a stage** (e.g. `/assignment-continue case-builder`), rewind to it: set `state.json.current_stage` to that stage, then tell the user which artifacts are now stale — everything that stage and later stages write, per the pipeline table in `CLAUDE.md`. **Do not delete them.** They stay as reference; the gates below refuse to trust them until they're regenerated.
5. Resume the pipeline at `current_stage` (stage order: `CLAUDE.md`), respecting the same HITL and loop-cap rules as `/assignment-new`.

## Rerunning from the middle

Re-running a stage rewrites its outputs and leaves every downstream artifact describing a draft that no longer exists. There is no invalidation bookkeeping to maintain — **the gates check freshness instead**:

- `formatter` is denied when `draft.json` is newer than `check_report.json`, because that PASS describes an older draft. Re-run `strict-checker` first.
- `research-planner` is denied while the Evidence Contract is unresolved.
- `strict-checker` is denied at loop 2, reading whichever of `state.loop_count` / `check_report.loop_number` is higher.

So the safe rewind is: set the stage, re-run forward, and let each gate tell you what still needs regenerating. If a gate blocks something you genuinely intend to skip, set `"gate_override": "<reason>"` in `state.json` and clear it afterwards.
