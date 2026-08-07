---
description: Show current stage, artifacts created, and loop count for the active assignment. Also regenerates WORKSPACE.md on demand.
---

1. Read the active assignment's `state.json`.
2. List which `workspace/*.md` files exist and which `OUTPUTS/*` files exist.
3. Stitch existing `workspace/*.md` files into `WORKSPACE.md` (order: intent → context → research_plan → research_* → synthesis → recommendations → tradeoffs → assumptions → devils_advocate → next_steps) — this is the only place `WORKSPACE.md` gets regenerated; it is a human-reading convenience, no agent reads it.
4. Report to the user in plain language: stage, loop_count, status, what's pending, outcome field if set.
