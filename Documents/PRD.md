# Assignment OS — Product Requirements Document (v0.2)

> Last updated: 2026-07-05. Supersedes v0.1.

---

## 1. Problem Statement

Interview assignments from companies are high-stakes, time-intensive, and evaluated on criteria that are often unstated. Current approaches either:
- Use generic AI assistance that produces polished output but misses what the company actually tests
- Rely on ad-hoc research with no quality gate and no reuse across assignments
- Generate output that looks good but doesn't optimize for the hiring signal

Result: technically competent submissions that miss evaluation criteria; wasted research not reusable later; no learning loop from outcomes.

---

## 2. Goals

| # | Goal |
|---|---|
| G1 | Maximize interview success rate, not just output quality |
| G2 | Identify and address the hiring signal, not just the stated assignment |
| G3 | Produce structured, reusable artifacts per assignment |
| G4 | Accumulate company and global knowledge across assignments over time |
| G5 | Keep human review focused on high-value decision points only |
| G6 | Operate within reasonable token and time budgets |
| G7 | Reuse company context intelligently; don't re-research what's already known |

## Non-Goals

- Building a generic document generator
- Auto-submitting without human review
- Replacing human judgment at critical decision points
- Optimizing output aesthetics at the cost of hiring signal coverage
- Supporting multiple users / SaaS (MVP: single operator, local)

---

## 3. Users

**Primary user:** The job seeker / PM candidate (you)

**Stakeholders modeled by agents:**
- Hiring manager / interviewer (what they're actually evaluating)
- Executive reviewer (VP/C-suite perspective on recommendations)
- Future-you (reusing company memory 6 months later)

---

## 4. User Stories

### Core flow
- I can paste an assignment and get a deliverable optimized for interview success, not just the literal question.
- I can provide optional context (screenshots, JD, competitor names, Figma) without being blocked if I don't have them.
- I am asked to confirm intent only when the system is uncertain — not after every stage.
- I must approve any additional research pass before it runs (protects token budget).
- I select which output formats to generate at the end, not upfront.
- I give final approval before any deliverable is submission-ready.
- I can stop and resume a pipeline at any stage without losing work.

### Memory and reuse
- Company context from a previous assignment loads automatically for the next at the same company.
- Stale company information is flagged and refreshed; stable info is reused.
- I can optionally provide outcome/feedback at assignment close; system updates memory.
- The system nudges me about retrospective at most twice, then moves on.

### Media and visual context
- I can add screenshots, PDFs, Figma exports, or screen recordings at any time.
- Media is analyzed once and cached — tokens are not burned re-analyzing the same image.
- The system uses metadata summaries for known images and only re-reads visuals when detail is needed.
- Old media is stored with timestamps so I know when it was captured.

### Quality
- Every claim in my deliverable is either cited or explicitly marked as an assumption.
- The system challenges its own recommendations before submitting to the quality gate.
- If auto-correction fails twice, the system escalates to me with the best available draft + unmet criteria list.

---

## 5. Functional Requirements

### FR1 — Session Management
- Session-start hook fires on every open: loads CLAUDE.md, reads state.json, pre-loads active assignment context and company memory
- System shows status on session open: current stage, what's waiting
- All session state persists in state.json; pipeline survives session restarts

### FR2 — Media Intake and Registry
- User adds media via `/media add [filepath]` or by placing files in a monitored location
- System copies file to `Companies/<Co>/media/` with timestamp prefix
- System analyzes once: vision for images, text extraction for PDFs
- System writes `.meta.json` per file: description, key elements, analysis summary, confidence, tokens used
- System updates `MEDIA_REGISTRY.json` with indexed entry per file
- Agent smart routing: read MEDIA_REGISTRY → read meta → decide metadata-sufficient vs re-analyze (re-analyze only if confidence < high OR question unanswerable from summary)
- Competitor media labeled separately in registry (`competitor: true, competitor_name: "..."`)
- Screen recordings: key-frame extraction at intervals; transcript if audio present

### FR3 — Input Collection
- User invokes `/assignment new [company]` to start
- System creates folder structure: `Companies/<Co>/<Assignment>/` + workspace/, OUTPUTS/, state.json, blank INPUT.md
- User pastes assignment text; system structures into INPUT.md (assignment, JD refs, media refs, competitor refs, constraints)
- INPUT.md is immutable after stage 2 completes

### FR4 — Hiring Signal Analysis
- System identifies what company is actually evaluating beyond stated question
- Output: core evaluation areas, company style signals, seniority signals, format expectations
- Uses `hiring-signal-patterns` skill
- Informs all downstream stages

### FR5 — Intent Contract
- System restates assignment as: goal, success criteria, audience, scope in/out, required formats, constraints, open questions, confidence score
- HITL triggered only if confidence < 0.75 OR intent is ambiguous
- User can confirm with one action or edit specific fields

### FR6 — Assignment Classification
- System identifies assignment type from 10 fixed templates
- Outputs: type, base_pipeline[], skip[], emphasis{}, complexity, estimated runtime
- Emphasis flags pass to receiving agents via their context contract
- New agent types added by: define contract in AGENT_CONTRACTS.md → add to template in `assignment-type-templates.md` skill

### FR7 — Execution Budget
- Before research begins, system shows user: complexity level, expected runtime, estimated searches, token tier
- User confirms proceed or adjusts
- Budget tracked in state.json; flagged if exceeded

### FR8 — Context Building
- System loads Company_Memory.md; freshness-checks each field by type
- Reuses valid fields; refreshes stale/missing fields via web research
- Builds context: company overview, products, competitors, interviewer profile, constraints
- Updates Company_Memory.md with new stable facts found

### FR9 — Research Planning
- System decomposes intent into research questions with objectives, sources, effort levels, parallelization flags, and success criteria
- Optional HITL: show plan to user for approval before research runs

### FR10 — Parallel Research
- Multiple subagents run concurrently with non-overlapping topic ownership
- Each subagent: bounded question, explicit scope, output format
- Each subagent: reads MEDIA_REGISTRY → meta → decides if re-analysis needed
- Findings include: claims, sources, confidence per claim, gaps identified

### FR11 — Research Gap Analysis
- Orchestrator inline call checks findings against plan success criteria
- If gaps: summarizes them, asks user: "Approve additional research pass?"
- If declined: proceeds; gaps flagged in open_questions.md and surfaced at final review

### FR12 — Insight Synthesis
- Compresses findings into insights with supporting evidence, confidence, and conflict flagging
- Tags each insight with implication for recommendation

### FR13 — Case Builder
- Builds recommendation, story, prioritization, tradeoffs
- Emits draft.json (structured content object — single source of truth for all formats)
- Emits Assumptions Register: every ungrounded claim labeled with rationale, confidence, falsifier
- Receives emphasis flags from Classifier via context contract

### FR14 — Devil's Advocate
- Fresh context, different instance from Case Builder
- Challenges draft: weaknesses, missing tradeoffs, likely interviewer objections
- One pass only; Case Builder does one revision pass
- Output surfaces in final review regardless

### FR15 — Strict Checker
- Tier 1 (all must pass, deterministic where possible): format present, all sub-questions addressed, citations present, no placeholder text, Assumptions Register present, hiring signal areas covered
- Tier 2 (≥ 0.8 each, LLM-graded with chain-of-thought): intent alignment, completeness, grounding, insight quality, consistency
- Tier 3 (qualitative advisory): audience fit, tone, format conventions
- On FAIL: routes to correct stage with specific fix instruction
- Max 2 correction loops; HITL escalation after 2 failures (best draft + unmet criteria)
- Loop detection: hash draft.json; near-identical to prior → stop + escalate

### FR16 — Executive Review
- Reviews from hiring-manager perspective: decisive, realistic, ROI clear, risks addressed, business impact obvious
- Advisory only — does not block pipeline
- Feedback surfaces at Final Review

### FR17 — Output Selection
- System presents options after checker PASS
- User selects from: Executive Summary, PPTX, Speaker Notes, DOCX, Appendix, FAQs, Interview Q&A, pitch scripts
- If INPUT.md specified outputs upfront: auto-generate those without this step

### FR18 — Formatting
- Runs only on Checker PASS
- All formats rendered from draft.json (single source of truth — consistency guaranteed)
- PPTX via PptxGenJS; DOCX via docx library; HTML via renderer
- Multiple formats run as parallel subagents

### FR19 — Visual QA
- Fresh subagent per format
- Checks: placeholder text, broken images, layout, slide count, branding, filename correctness
- Issues → back to Formatter (not counted as Checker loop)

### FR20 — Final Review
- Mandatory HITL: presents all deliverables + qa_report + executive review notes
- User approves → state.json marked complete; Company_Memory.md updated
- Partial approval (approve PPTX, reject DOCX) → Formatter re-runs rejected formats

### FR21 — Retrospective
- Orchestrator nudges user max 2 times (tracked via state.json.hitl_nudge_count)
- If provided: updates MEMORY.md → Company_Memory.md → Global/memory/
- If declined after 2 nudges: skip silently

---

## 6. Non-Functional Requirements

### NFR1 — Token Efficiency
- Context contracts: each agent declares exactly which workspace/ files it reads — nothing more
- Workspace Manager is the ONLY writer to workspace/ — no duplicate context loading
- Every large artifact has an analysis_summary; agents default to summary unless full content needed
- Media reuse: metadata-first, re-analyze only when insufficient
- Execution budget shown upfront; research expansion requires explicit approval
- Effort scaling: complexity drives agent count

### NFR2 — Durability
- Checkpoint after each stage via state.json
- Resume from last checkpoint on session restart or failure
- No state lives only in memory or in-context — always persisted to file

### NFR3 — Cost Predictability
- Budget estimate shown before run (complexity → token tier)
- Research expansion requires user approval every time
- Max 2 auto-correction loops per run

### NFR4 — Auditability
- Every Checker verdict logged with per-criterion evidence
- Every assumption in Assumptions Register traceable to source
- Every loop logged with token cost estimate
- workspace/ section files are the canonical record of all decisions

### NFR5 — Maintainability
- One responsibility per agent; one responsibility per slash command
- Composable prompts; no monolithic agent prompts
- Typed JSON artifacts between stages; schema in AGENT_CONTRACTS.md
- Model swappable per agent without pipeline changes

### NFR6 — Reliability
- Loop-detection guard (hash-based)
- Graceful degradation: deliver best available draft + unmet criteria list rather than infinite spin
- HITL escalation path for every failure mode
- Pre-file-read hook enforces context contracts — no agent reads outside its scope

---

## 7. Data Model

| Artifact | Format | Owner (writes) | Consumers (reads) |
|---|---|---|---|
| `INPUT.md` | Markdown | Intake Agent | All agents |
| `state.json` | JSON | Orchestrator (all stages) | Orchestrator, hooks |
| `MEDIA_REGISTRY.json` | JSON | Media Analysis Agent | All agents needing visuals |
| `<file>.meta.json` | JSON | Media Analysis Agent | Research Executor, Context Builder |
| `workspace/intent.md` | Markdown | Workspace Manager | Intent Agent → all downstream |
| `workspace/hiring_signal.md` | Markdown | Workspace Manager | All agents |
| `workspace/classifier.md` | Markdown | Workspace Manager | Orchestrator, Case Builder |
| `workspace/context.md` | Markdown | Workspace Manager | Research Planner, Case Builder |
| `workspace/research_plan.md` | Markdown | Workspace Manager | Research Executor |
| `workspace/research_<qid>.md` | Markdown | Workspace Manager | Insight Synthesizer |
| `workspace/synthesis.md` | Markdown | Workspace Manager | Case Builder |
| `workspace/assumptions.md` | Markdown | Workspace Manager | Checker |
| `workspace/recommendations.md` | Markdown | Workspace Manager | Devil's Advocate, Exec Reviewer |
| `workspace/tradeoffs.md` | Markdown | Workspace Manager | Checker |
| `workspace/devils_advocate.md` | Markdown | Workspace Manager | Case Builder (revision pass) |
| `workspace/executive_review.md` | Markdown | Workspace Manager | Final Review |
| `draft.json` | JSON | Case Builder | Checker, Formatter |
| `check_report.json` | JSON | Strict Checker | Orchestrator |
| `qa_report.json` | JSON | Visual QA | Orchestrator, Final Review |
| `OUTPUTS/<files>` | Binary/HTML | Formatter | Visual QA, Final Review |
| `MEMORY.md` | Markdown | Workspace Manager | Company Memory (retrospective) |
| `Company_Memory.md` | Markdown | Context Builder, Retrospective | Context Builder |
| `Global/memory/` | Markdown files | Retrospective | All agents globally |
| `WORKSPACE.md` | Markdown | Workspace Manager | Human view only — not read by agents |

---

## 8. Key JSON Schemas

### draft.json (critical — all formatters depend on this)

```json
{
  "title": "string",
  "audience": "string",
  "assignment_type": "string",
  "sections": [
    {
      "id": "s1",
      "type": "executive_summary|problem|insight|recommendation|prioritization|metrics|risks|tradeoffs|appendix",
      "heading": "string",
      "content": "string",
      "supporting_data": ["string"],
      "citations": [
        { "claim": "string", "source": "string", "url": "string | null" }
      ],
      "slide_notes": "string | null",
      "is_assumption": false
    }
  ],
  "assumptions_register": [
    {
      "assumption": "string",
      "rationale": "string",
      "confidence": 0.85,
      "falsifier": "string",
      "source_type": "grounded|ungrounded"
    }
  ],
  "metadata": {
    "version": 1,
    "created": "ISO datetime",
    "assignment_type": "string",
    "word_count_estimate": 0,
    "checker_loop": 0
  }
}
```

### check_report.json

```json
{
  "verdict": "PASS|FAIL",
  "loop_number": 1,
  "tier1": {
    "all_pass": true,
    "checks": [
      { "criterion": "string", "verdict": "PASS|FAIL", "evidence": "string", "deterministic": true }
    ]
  },
  "tier2": {
    "all_above_threshold": true,
    "threshold": 0.8,
    "scores": [
      { "criterion": "string", "score": 0.85, "reasoning": "string", "verdict": "PASS|FAIL" }
    ]
  },
  "tier3": { "notes": ["string"] },
  "routing": {
    "route_to": "research|case_builder|intake|formatter|null",
    "reason": "string",
    "specific_fix": "string"
  },
  "unmet_criteria": ["string"]
}
```

### state.json

```json
{
  "assignment_id": "string",
  "company": "string",
  "assignment_name": "string",
  "current_stage": "string",
  "loop_count": 0,
  "last_checkpoint": "ISO datetime",
  "hitl_nudge_count": 0,
  "status": "active|complete|paused|failed",
  "selected_outputs": ["string"],
  "budget": {
    "complexity": "low|medium|high",
    "estimated_runtime_minutes": 0,
    "approved": true
  }
}
```

---

## 9. Success Metrics

| Metric | Target | How measured |
|---|---|---|
| Goal-coverage rate | ≥ 85% | Human audit of delivered artifacts |
| Checker-human agreement (κ) | ≥ 0.6 | Labeled example set |
| False-pass rate | Near zero (Tier 1) | Human post-review audit |
| First-pass yield | Track and optimize | Logged per run in state.json |
| Citation accuracy | Track | Manual spot-check |
| Token cost per run | Track; flag outliers | Logged per stage |
| Human edit distance on output | Track; lower = better | Diff after delivery |
| Time-to-first-value | Track | Clock from `/assignment new` to draft.json |

---

## 10. Risks

| Risk | Mitigation |
|---|---|
| Checker false-pass | Hiring signal in Tier 1 hard gates; Opus for checker; independent model |
| Token blowup | Budget shown upfront; research expansion manual; 2-loop cap |
| Intent drift | Intent Contract + HITL confirmation |
| Hallucinated stats | Assumptions Register + citation check in Tier 1 |
| Stale company memory | Freshness metadata + refresh cadence per field type |
| Over-engineering | Default to chain; add parallelism only when genuinely needed |
| Lost work on failure | state.json checkpoint after every stage |

---

## 11. Open Items (to resolve during build)

| # | Item | Resolution path |
|---|---|---|
| 1 | Max concurrent subagents in Claude Code | Test with 3, 5, 10 parallel; cap based on result |
| 2 | Confidence threshold for Intent HITL | Start at 0.75; calibrate on first 5 real assignments |
| 3 | PptxGenJS setup + wrapper | Confirm installed; write tool wrapper in Phase 1 |
| 4 | DOCX library selection | Evaluate `docx` npm package for environment |
| 5 | LibreOffice/Playwright for PPTX→image | Confirm setup for Visual QA rendering |
| 6 | Screen recording handling (key frames vs transcript) | Build frame-extraction first; add transcript if recordings common |
| 7 | writing-style.md content | User writes personal voice/preferences before first run |
| 8 | hiring-signal-patterns.md content | Seed with known patterns; improve after each assignment |
| 9 | checker-rubrics.md content per type | Start with 3 most common types; expand as needed |

---

## 12. Out of Scope (MVP)

- Multiple users / SaaS
- Web UI / API server  
- Scheduled / async job processing
- Auto-submission to companies
- Minority-veto ensemble checker
- Judge-alignment recalibration loop
- Self-improving prompts from logged failures

---

## 13. Implementation Order

1. CLAUDE.md + hooks (settings.json) + slash commands — project foundation
2. Skill files (Global/skills/) — seed content before agents use them
3. AGENT_CONTRACTS.md — schemas before any agent is coded
4. Build agents in pipeline order (see ARCHITECTURE.md Phase 2)
5. Test with one real assignment end-to-end
6. Iterate
