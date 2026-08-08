---
description: Start a new assignment — creates folder structure and runs the pipeline through the first HITL gate.
---

Company/assignment name from `$ARGUMENTS` (ask if not given).

1. Create `Companies/<Company>/<YYYY-MM-DD>_<AssignmentName>/{workspace/,OUTPUTS/}` and `Companies/<Company>/{Company_Memory.md, MEDIA_REGISTRY.json}` if they don't exist.
2. Write `state.json`:
```json
{ "assignment_id": "...", "company": "...", "assignment_name": "...", "current_stage": "intake_intent", "loop_count": 0, "last_checkpoint": "ISO datetime", "status": "active", "selected_outputs": [], "skipped_stages": [], "outcome": "pending" }
```
3. Ask the user for the assignment text, JD (optional), interviewer info (optional), competitors (optional), constraints (optional). If media files are mentioned, tell them to run `/media-add <path>` first.
4. Invoke the `intake-intent` agent with the collected input.
5. If it returns `hitl_needed: true` → stop and run `/intent-confirm`. Otherwise proceed to the `research-planner` agent, then continue the pipeline stage by stage, updating `current_stage` and `last_checkpoint` in `state.json` after each one.
   - **Research fan-out:** after `research-planner` writes the plan, spawn **one `research-executor` per question**, in parallel, passing each instance only its own question block. Cap concurrency at **4** — the one prior real run hit a session limit at 6 and had to re-run the failed questions. If there are more than 4 questions, run them in batches.
   - **Decide before arguing:** once every `research_<qid>.md` exists, run `decision-builder`, then `case-builder`. Never skip straight to `case-builder` — a gate blocks it when `workspace/decision.md` is missing, because arguing first is what produces rejected alternatives written as after-the-fact justification.
   - **AI justification (conditional):** after `case-builder`, grep `draft.json` for AI/ML terms (LLM, model, agent, copilot, recommendation engine, semantic, embedding, RAG, ranking, classifier, prediction, personalis/z, "AI-"). If any hit, run `ai-justification` in the same batch as the panel. If none, skip it — most assignments propose no AI and the stage would find nothing. The agent self-exits cheaply if the grep was a false positive, so err toward running it.
   - **Panel fan-out:** after `case-builder`, run the 5 `panel-reviewer` personas batched **4 then 1** (`founder`, `engineer`, `compliance`, `ai_smell`, then `peer_pm`), one persona per instance. If budget forces four, drop `peer_pm` — it judges how the case reads, not whether it's right.
   - **If the panel attacks the decision** rather than the argument for it, route back to `decision-builder`, not to `case-builder`. `case-builder` reports this as `decision_disputed: true` rather than silently re-deciding.
   - **Optional stages:** if `state.json.optional_stages` contains `exec_review`, run the `executive-reviewer` agent after `strict-checker` PASSes and surface its notes to the user. It is advisory and never blocks `formatter`.
6. Before `strict-checker`'s first PASS routes to `formatter`, run `/output-select` if `selected_outputs` is still empty.
7. Enforce always: never start `formatter` before `check_report.json.verdict == "PASS"`; if `strict-checker` FAILs twice (`loop_count == 2`), stop and surface the best draft + unmet criteria to the user instead of looping again.
