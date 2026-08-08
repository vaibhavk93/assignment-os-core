---
description: HITL gate — confirm the Intent Contract and resolve the Evidence Contract before research begins.
---

1. Show the user `workspace/intent.md` in full, plus the confidence score and any open questions from `intake-intent`.
2. Ask them to confirm as-is or request edits.
3. On edits, rewrite `workspace/intent.md` with the confirmed version — this becomes ground truth for every downstream agent.
4. **Resolve `workspace/evidence_contract.md`.** Show the table and walk the user through it row by row. Every row must end as `supplied` or `waived`:
   - **supplied** — they give you the asset. Register media via `/media-add` so it lands in `MEDIA_REGISTRY.json`; paste text/links straight into the row. Then actually use it downstream — an asset collected and ignored is worse than one never requested.
   - **waived** — they can't or won't. Keep the row's consequence text verbatim; it becomes a labelled assumption in the deliverable, and `case-builder` must carry it into `assumptions_register` with the confidence the row states.
   Do not soften a consequence to make waiving feel easier. The point of the row is that the user chooses with the cost visible.
5. Rewrite `evidence_contract.md` with final statuses, then set `"evidence_contract": {"status": "resolved"}` in `state.json`. `research-planner` is blocked by `gate_check.py` until this is set.
6. Update `state.json.current_stage` to `research_planner` and proceed.
