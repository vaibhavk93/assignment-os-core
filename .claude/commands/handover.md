---
description: Update HANDOFF.md with current state before ending a session, so a fresh Claude instance can resume with full context.
---

Rewrite `HANDOFF.md` (current-state only — do not append to a growing session log; overwrite the Active Assignment and Pending Actions sections):
1. Active Assignment table: company, folder, type, pipeline status, loop_count, outputs delivered, outcome.
2. Pending Actions (User Must Do): anything blocked on the user.
3. Known Issues / Gotchas: anything a fresh session would trip over.

Keep it under 60 lines. Historical "what happened this session" narrative belongs in commit messages and `MEMORY.md`, not here — `HANDOFF.md` is where-we-are, not a diary.
