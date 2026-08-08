---
description: Opt-in — build the live-defence rehearsal kit for an assignment that got an interview.
---

Assignment path from `$ARGUMENTS`, or the most recently completed one if not given. Run this when an interview is actually scheduled, not before — it is an expensive pass and an unshortlisted submission never needs it.

1. Confirm `draft.json` and `OUTPUTS/` exist for that assignment. If not, the pipeline hasn't finished — say so and stop. A `status: complete` assignment is the normal case here, not an error.
2. Add `interview_prep` to `state.json.optional_stages`. Leave `status`, `current_stage`, and `loop_count` untouched — this runs beside the pipeline, not inside it.
3. Run the `interview-prep` agent. It reads what is already on disk and re-runs nothing upstream.
4. Point the user at `OUTPUTS/interview_prep.md` and tell them to run `/debrief` after the interview.
