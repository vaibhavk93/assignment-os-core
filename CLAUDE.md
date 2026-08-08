# Assignment OS — Project Brain

## What This Is

An Assignment Operating System for interview assignments. Every assignment runs through a 7-stage pipeline that identifies the hiring signal, researches evidence, builds a recommendation, quality-gates it, and produces delivery-ready output.

**Optimization target:** Interview success (hiring signal coverage) — not output aesthetics. `/debrief` after each real interview is what actually measures this; run it every time.

---

## Session Start Ritual

1. Read `state.json` in the most recently active assignment folder (if any).
2. If `status == "active"` → load `Companies/<Company>/Company_Memory.md` + `workspace/intent.md`, show stage/pending/loop_count.
3. No active assignment → greet and suggest `/assignment-new <Company>`.

---

## Folder Structure

```
Assignment OS/
  CLAUDE.md
  HANDOFF.md                   ← where we left off (current state only)
  .claude/
    agents/                    ← 7 pipeline agents + 1 optional (executive-reviewer)
    commands/                  ← 8 slash commands
    skills/                    ← 6 knowledge packs (progressive disclosure — read on demand)
  Documents/
    AGENT_CONTRACTS.md         ← per-agent contracts (build spec)
    PRD.md
    archive/                   ← superseded specs, kept for reference only
  Global/
    candidate/VOICE.md         ← candidate voice profile, cross-assignment
    memory/                    ← cross-assignment learnings
    scripts/                   ← pptx_builder.py etc.
  Companies/<Company>/
    MEDIA_REGISTRY.json
    media/
    Company_Memory.md
    <Assignment>/
      INPUT.md                 ← immutable
      workspace/                ← machine-readable, agent I/O
      WORKSPACE.md             ← human-reading only, regenerated on demand by /assignment-status
      OUTPUTS/
      MEMORY.md                ← learnings + /debrief outcome
      state.json
```

---

## The Pipeline (7 stages)

| # | Agent | Merges (history) | Reads → Writes |
|---|---|---|---|
| 1 | `intake-intent` | Intake + Hiring Signal + Intent | user input → `INPUT.md`, `workspace/intent.md`, `workspace/evidence_contract.md` |
| 2 | `research-planner` | Classifier + Context Builder + Research Planner | `intent.md` → `context.md`, `research_plan.md` |
| 3 | `research-executor` | (unchanged, parallel) | one question → `research_<qid>.md` |
| 4 | `case-builder` | Insight Synthesizer + Case Builder | `research_*.md` → `draft.json` |
| 5 | `panel-reviewer` | replaces Devil's Advocate — 5 stakeholder personas | draft → `panel_<persona>.md` |
| 6 | `strict-checker` | (unchanged) | draft → `check_report.json` (PASS/FAIL gate) |
| 7 | `formatter` | Formatter + Visual QA | `draft.json` → `OUTPUTS/*`, self-checked |

Optional, opt-in, both advisory and non-blocking, both skipped by default:
- `executive-reviewer` (via `/output-select`) runs after a Checker PASS — only worth it for genuinely executive audiences.
- `interview-prep` (via `/interview-prep`) runs after Formatter, whenever an interview is actually scheduled — including on an assignment already marked `complete`. Reads the finished draft, writes `OUTPUTS/interview_prep.md`, re-runs nothing. Off by default because it's an opus-tier read of every artifact, and most submissions never get shortlisted.

Stage 3 fans out: one `research-executor` per question, in parallel, **max 4 concurrent** (a prior run hit a session limit at 6).

Stage 5 fans out too: 5 personas, batched **4 then 1** (`founder`, `engineer`, `compliance`, `ai_smell`, then `peer_pm`) to stay under the same 4-concurrent cap. If budget forces four, drop `peer_pm` — it judges how the case reads, not whether it's right.

## Agent return values

Every agent's real output is the **file it writes**. Its return message is a receipt, not a report: emit the JSON in that agent's `## Returns` block and nothing else — no prose summary, no restating what's already in the file, no markdown tables. The orchestrator reads the file when it needs detail. A subagent that narrates its work back pays for the same content twice.

---

## Critical Rules (enforce always)

The first two are **enforced in code**, not on the honour system: a `PreToolUse` hook in `.claude/settings.json` runs `Global/scripts/gate_check.py` on every agent call and denies the ones below before the agent spawns.

- **Evidence gate:** `research-planner` never runs while `workspace/evidence_contract.md` exists and `state.json.evidence_contract.status != "resolved"`. Written by `intake-intent`, resolved row-by-row at `/intent-confirm`. Every row ends `supplied` or `waived`, and a waived row's consequence is carried verbatim into the deliverable's assumptions. Researching around an artifact nobody looked at is how a 0.4-confidence assumption ends up under the lead recommendation.
- **Freshness (applies to every gate below):** each stage's output is *evidence about the input it read*. Rewinding regenerates an input and silently strands the outputs derived from it. Gates therefore compare mtimes along the chain `intent.md → research_plan.md → research_<qid>.md → draft.json → check_report.json`, and refuse to trust anything older than its own source. There is no dirty-flag bookkeeping to maintain — the filesystem already records what changed, which is why this can't drift the way a hand-written dependency map does.
- **Case Builder gate:** blocked when `research_plan.md` predates `intent.md`, or when any `research_<qid>.md` predates `research_plan.md` — the denial names exactly which questions to re-run.
- **Formatter gate:** never runs unless `check_report.json.verdict == "PASS"` **and** that report is at least as new as `draft.json`. Non-negotiable.
- **Loop cap:** `state.json.loop_count` reaching 2 on a Checker FAIL → surface HITL immediately, never a third auto-loop.
- **Deliberate override:** set `"gate_override": "<reason>"` in the assignment's `state.json` to bypass either gate. Requires opening the file and writing a reason, so it can't be tripped by accident. Clear it once you're past the exception.
- **Research expansion:** never run an extra research pass without explicit user approval.
- **Media efficiency:** check `MEDIA_REGISTRY.json` → `.meta.json` first; re-analyze the image only if `analysis_confidence != "high"` or the summary can't answer the question.
- **INPUT.md is immutable** once written by `intake-intent`.

---

## Slash Commands

| Command | Purpose |
|---|---|
| `/assignment-new [Company]` | Start a new assignment |
| `/assignment-continue` | Resume from last checkpoint |
| `/assignment-status` | Show stage/loop/pending; regenerates WORKSPACE.md |
| `/media-add [filepath]` | Register a media file |
| `/intent-confirm` | HITL — confirm/edit Intent Contract |
| `/output-select` | HITL — choose output format(s), opt into exec review |
| `/interview-prep` | Opt-in — rehearsal kit for an assignment that got an interview |
| `/debrief [assignment]` | Record real interview outcome — closes the feedback loop |
| `/handover` | Rewrite HANDOFF.md before ending a session |

---

## Skills (`.claude/skills/`, loaded on demand)

| Skill | Used by |
|---|---|
| `hiring-signal-patterns` | intake-intent, case-builder, panel-reviewer, strict-checker |
| `pm-frameworks` | intake-intent, research-planner, case-builder |
| `checker-rubrics` | strict-checker |
| `research-heuristics` | research-planner, research-executor |
| `assignment-type-templates` | research-planner, strict-checker |
| `deck-builder` | case-builder (structure), formatter (rendering) |
| `voice-and-brevity` | case-builder (write-time limits), strict-checker (enforcement via `checker-rubrics`) |

---

## State Management

`state.json` fields: `current_stage`, `loop_count`, `status` (active\|complete\|paused\|failed), `selected_outputs`, `optional_stages`, `outcome` (pending\|advanced\|rejected — set by `/debrief`), `evidence_contract` (`{status: pending|resolved}` — gates `research-planner`).

`gate_check.py` resolves "the active assignment" as the most recently modified `state.json` whose `status` is **not** `complete` — plain mtime would let a `/debrief`-ed old assignment hijack the gate for a live run.

---

## Architecture Reference

`Documents/AGENT_CONTRACTS.md` — full per-agent contracts (build spec). `Documents/PRD.md` — product requirements. `Documents/archive/` — superseded 17-stage architecture, kept for history only, do not treat as current.
