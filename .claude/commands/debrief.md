---
description: Record the real interview outcome after the fact — the only step that closes the feedback loop on the system's actual goal (interview success, not rubric compliance).
---

Assignment path from `$ARGUMENTS`, or the most recently completed one if not given.

1. Ask the user: did the candidate advance? (advanced/rejected/pending). What did the interviewer actually ask, versus what `OUTPUTS/interview_prep.md` (if it was run) or the draft predicted? Any direct feedback received?
2. Update `state.json`: `"outcome": "advanced|rejected|pending"`.
3. Append to that assignment's `MEMORY.md`:
```markdown
## Outcome (added via /debrief on <date>)
- Result: advanced|rejected|pending
- Interviewer feedback: ...
- Predicted vs actual questions: ...
```
4. If there's a real, non-obvious learning (a hiring-signal read that was right or wrong, a pattern likely to recur), append one dated entry to the "Learnings Log" section at the bottom of `.claude/skills/hiring-signal-patterns/SKILL.md`. Keep it to 2-3 lines — this is the mechanism that makes the next assignment's hiring-signal analysis better than this one's. Don't append speculative or low-confidence learnings.
