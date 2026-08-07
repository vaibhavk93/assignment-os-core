---
description: HITL gate — confirm or edit the Intent Contract before research begins.
---

1. Show the user `workspace/intent.md` in full, plus the confidence score and any open questions from `intake-intent`.
2. Ask them to confirm as-is or request edits.
3. On edits, rewrite `workspace/intent.md` with the confirmed version — this becomes ground truth for every downstream agent.
4. Update `state.json.current_stage` to `research_planner` and proceed.
