# Assignment OS — Project Brain

## What This Is

An Assignment Operating System for interview assignments. Every assignment runs through a multi-agent pipeline that identifies the hiring signal, researches evidence, builds a recommendation, quality-gates it, and produces delivery-ready output.

**Optimization target:** Interview success (hiring signal coverage) — not output aesthetics.

---

## Session Start Ritual (do this every session)

1. Read `state.json` in the most recently active assignment folder (if any)
2. If `state.json.status == "active"`:
   - Load `Companies/<Company>/Company_Memory.md`
   - Load `Companies/<Company>/<Assignment>/workspace/intent.md`
   - Show user: current stage, what's pending, loop count
3. If no active assignment: greet user and suggest `/assignment-new <Company>`

---

## Folder Structure

```
Assignment OS/
  CLAUDE.md                    ← this file (project brain)
  .claude/
    agents/                    ← agent definition files
    commands/                  ← slash command definitions
    settings.json              ← hooks
  Documents/                   ← architecture, PRD, agent contracts
  Global/
    skills/                    ← reusable knowledge packs (loaded into agent prompts)
    memory/                    ← global learnings across all assignments
  Companies/
    <Company>/
      MEDIA_REGISTRY.json      ← index of all media for this company
      media/                   ← screenshots, PDFs, recordings (timestamped)
      Company_Memory.md        ← reusable company knowledge
      <Assignment>/
        INPUT.md               ← immutable: assignment text, refs, constraints
        WORKSPACE.md           ← human-readable merged view (auto-generated)
        workspace/             ← machine-readable section files (what agents read)
        OUTPUTS/               ← final deliverables
        MEMORY.md              ← reusable learnings from this assignment
        state.json             ← pipeline state, loop count, checkpoint
```

---

## Critical Rules (enforce always)

### Context contracts
Every agent reads ONLY the workspace/ section files listed in its contract (see `Documents/AGENT_CONTRACTS.md`). **Agents never load full WORKSPACE.md** — it is for human reading only. If an agent asks to read a file outside its contract, refuse and redirect it to the correct files.

### Single writer
**Only Workspace Manager writes to workspace/ section files.** All other agents return their output as content to Workspace Manager, which writes it and regenerates WORKSPACE.md. Never let two agents write to the same workspace file.

### Formatter gate
**Formatter never runs unless `check_report.json.verdict == "PASS"`.** This is non-negotiable.

### Loop cap
Track `state.json.loop_count`. If it reaches 2 on a Checker FAIL, surface HITL immediately — never auto-loop a third time.

### Research expansion
**Never run an additional research pass without explicit user approval.** Always ask first.

### Media efficiency
When agents need visual context, always check `MEDIA_REGISTRY.json` → `.meta.json` first. Re-analyze the actual image only if `analysis_confidence != "high"` OR the question cannot be answered from `analysis_summary`.

---

## Available Slash Commands

| Command | Purpose |
|---|---|
| `/assignment-new [Company]` | Start a new assignment (creates folder structure, runs pipeline) |
| `/assignment-continue` | Resume paused/failed assignment from last checkpoint |
| `/assignment-status` | Show current stage, artifacts created, loop count |
| `/media-add [filepath]` | Process and register a new media file into the company registry |
| `/research-approve` | Approve an additional research pass (HITL gate) |
| `/intent-confirm` | Confirm or edit the Intent Contract (HITL gate) |
| `/output-select` | Choose output formats before Formatter runs (HITL gate) |

---

## Agent Overview (pipeline order)

| # | Agent | File | Purpose |
|---|---|---|---|
| 0 | Orchestrator | slash commands | Drives pipeline, manages state, HITL routing |
| 1 | Media Analysis | `agents/media-analysis.md` | Analyzes + registers media files |
| 2 | Intake | `agents/intake.md` | Writes INPUT.md from user input |
| 3 | Workspace Manager | `agents/workspace-manager.md` | Only agent that writes workspace/ files |
| 4 | Hiring Signal Analyzer | `agents/hiring-signal-analyzer.md` | Identifies what company is actually testing |
| 5 | Intent Agent | `agents/intent-agent.md` | Writes Intent Contract |
| 6 | Classifier | `agents/classifier.md` | Selects pipeline template + skip/emphasis |
| 7 | Context Builder | `agents/context-builder.md` | Builds company/product context |
| 8 | Research Planner | `agents/research-planner.md` | Decomposes intent into research questions |
| 9 | Research Executor | `agents/research-executor.md` | Executes one bounded research question |
| 10 | Insight Synthesizer | `agents/insight-synthesizer.md` | Turns findings into insights |
| 11 | Case Builder | `agents/case-builder.md` | Builds draft.json + assumptions |
| 12 | Devil's Advocate | `agents/devils-advocate.md` | Challenges the recommendation |
| 13 | Strict Checker | `agents/strict-checker.md` | Quality gate — PASS/FAIL |
| 14 | Executive Reviewer | `agents/executive-reviewer.md` | Advisory executive lens |
| 15 | Formatter | `agents/formatter.md` | Renders to PPTX/DOCX/HTML |
| 16 | Visual QA | `agents/visual-qa.md` | Bug-hunts formatted output |

---

## Skills (knowledge packs — loaded into agent prompts)

| File | Used by |
|---|---|
| `Global/skills/hiring-signal-patterns.md` | Hiring Signal Analyzer, Devil's Advocate, Exec Reviewer, Case Builder |
| `Global/skills/assignment-type-templates.md` | Classifier, Research Planner |
| `Global/skills/pm-frameworks.md` | Intent Agent, Research Planner, Insight Synthesizer, Case Builder |
| `Global/skills/writing-style.md` | Case Builder |
| `Global/skills/presentation-style.md` | Case Builder, Formatter |
| `Global/skills/research-heuristics.md` | Research Planner, Context Builder, Research Executor |
| `Global/skills/checker-rubrics.md` | Strict Checker |
| `Global/skills/brand-templates.md` | Formatter |

---

## State Management

`state.json` is the source of truth for pipeline state. After every stage, update it. Key fields:
- `current_stage` — what just completed
- `loop_count` — how many Checker correction loops have run
- `status` — active | complete | paused | failed
- `hitl_nudge_count` — retrospective nudges sent

---

## Architecture Reference

Full specs in `Documents/`:
- `ARCHITECTURE.md` — system design
- `PRD.md` — product requirements
- `AGENT_CONTRACTS.md` — per-agent input/output schemas and guardrails
