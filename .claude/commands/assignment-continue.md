---
description: Resume a paused or failed assignment from its last checkpoint.
---

1. Find the most recently modified `state.json` under `Companies/**` with `status` in `active`/`paused`/`failed` (or use `$ARGUMENTS` as an explicit assignment path if given).
2. Read it, plus `Companies/<Company>/Company_Memory.md` and `workspace/intent.md`.
3. Report to the user: current stage, what's pending, loop count, any open questions.
4. Resume the pipeline at `current_stage` (see stage order in the project `CLAUDE.md`), respecting the same HITL and loop-cap rules as `/assignment-new`.
