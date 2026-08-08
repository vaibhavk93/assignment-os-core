# Assignment OS — Agent Contracts (v0.2 — 7-stage pipeline)

> Build specification for the 7 agents in `.claude/agents/`. The prompt files there are the executable version of these contracts — this doc explains the *why* behind merges and cuts; the agent files are the source of truth for exact behavior.

Superseded: v0.1 defined 17 agents. Merged down to 7 because (a) research on multi-agent systems shows each extra stage costs tokens roughly linearly while adding a lossy handoff, and (b) the one real run (Ixigo, see `Companies/Ixigo/.../MEMORY.md`) showed which stages carried their weight and which were ceremony. Full v0.1 text is in `Documents/archive/AGENT_CONTRACTS_v0.1.md` for reference.

---

## Merges and cuts, and why

| New agent | Absorbed | Reasoning |
|---|---|---|
| `intake-intent` | Intake, Hiring Signal Analyzer, Intent Agent | All three read only `INPUT.md`-level content and write one contract. No reason to hand off between them — it's one reasoning chain. |
| `research-planner` | Classifier, Context Builder, Research Planner | Classification is a ~5-line decision that was its own agent; context-building and planning both consume `intent.md` and produce planning artifacts. Merging removes 2 handoffs. |
| `research-executor` | — | Unchanged. Proven: parallel instances, strict topic ownership, this was the highest-value stage in the one real run. |
| `case-builder` | Insight Synthesizer, Case Builder | Synthesis existed only to feed Case Builder immediately after; no other consumer needed the intermediate file as a stable artifact. |
| `panel-reviewer` | Replaces `devils-advocate` | Five stakeholder personas (founder, engineer, compliance, peer_pm, ai_smell), one per instance, batched 4 then 1. The single-lens version caught 3 high-severity issues before Checker in the one real run; the panel widens that to stakes a single interviewer lens misses. Fresh-context requirement preserved. |
| `strict-checker` | — | Unchanged. The gate. Rubric already strong (see `checker-rubrics` skill). |
| `formatter` | Formatter, Visual QA | Visual QA existed only to bug-hunt Formatter's own output one step later — folded into a self-check pass in the same agent. |

**Cut entirely, not merged:**
- **Workspace Manager** — its job (single-writer discipline) is now structural: each agent writes its own named file directly, no separate write-broker agent needed. Still enforced by convention (see below), just not by a dedicated agent call.
- **Media Analysis as a pipeline stage** — made on-demand only (`/media-add`), since most assignments have no media and the stage added a mandatory check on every run for a mostly-empty registry.
- **Executive Reviewer** — was skipped in the only real run (no JD to calibrate against). Now opt-in via `/output-select`, not a default stage.
- **Budget Estimate** — `state.json.budget` was never read or enforced anywhere in the pipeline; removed rather than fixed, since nothing depended on it.

**Single-writer rule, preserved without an agent:** each agent's contract names exactly one file (or file set) it writes. No two agents ever target the same `workspace/*.md` path. This was previously enforced by routing all writes through Workspace Manager; it's now enforced by the contracts below simply not overlapping.

---

## Current Contracts

Full detail (model, tools, exact output schema, guardrails, failure modes) lives in each agent's frontmatter + body under `.claude/agents/`:

- `.claude/agents/intake-intent.md` — model: opus. Writes `INPUT.md`, `workspace/intent.md`.
- `.claude/agents/research-planner.md` — model: sonnet. Writes `workspace/context.md`, `workspace/research_plan.md`, updates `Company_Memory.md`.
- `.claude/agents/research-executor.md` — model: sonnet (haiku for simple lookups). Writes `workspace/research_<qid>.md`. One instance per question, run in parallel.
- `.claude/agents/case-builder.md` — model: sonnet. Writes `draft.json`, `workspace/recommendations.md`, `workspace/assumptions.md`, `workspace/tradeoffs.md`, `workspace/synthesis.md`.
- `.claude/agents/panel-reviewer.md` — model: sonnet, fresh context, one persona per instance. Writes `workspace/panel_<persona>.md`.
- `.claude/agents/strict-checker.md` — model: opus, fresh context. Writes `check_report.json`. Gates `formatter`.
- `.claude/agents/formatter.md` — model: haiku. Writes `OUTPUTS/*`, `qa_report.json`.

## Skill Files (Reference)

Skills live in `.claude/skills/<name>/SKILL.md` (progressive disclosure — frontmatter loaded at session start, body read on demand). See `CLAUDE.md` for the skill → consumer table.

## Open Items

1. **Confidence threshold for intake-intent HITL** — triggers at 0.75; revalidate after a few more real runs (n=1 currently).
2. **Loop detection hash** — `draft.json` content excluding `metadata.created`/`metadata.version`.
3. **Research executor concurrency** — session limit was hit at 6 parallel in the one real run; start conservatively (3–4) and increase if stable.
4. **`/debrief` learnings log** — first real test of whether appending to `hiring-signal-patterns` actually improves the next run's signal-reading. Revisit after 3–5 debriefs.
