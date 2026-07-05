# Assignment OS — Agent Contracts (v0.1)

> Defines every agent: responsibility, model, context contract (exactly what it reads), output schema, guardrails, and failure modes.
> These schemas are the build specification. No agent is coded before its contract is finalized here.

---

## Contract Format

Each agent contract specifies:
- **Responsibility** — one sentence
- **Model** — which model and why
- **Context contract** — exactly which files the agent reads (nothing else)
- **Skills** — which skill files are injected into the prompt
- **Tools** — which tools the agent may call
- **Output** — what it writes (file path + JSON schema or markdown structure)
- **Returns to orchestrator** — lightweight signal for routing
- **Guardrails** — hard constraints on behavior
- **Failure modes** — what can go wrong and what happens

---

## Agent 0 — Orchestrator

**Responsibility:** Drives the full pipeline; manages state, HITL checkpoints, routing on failures, and loop counting.

**Model:** Not an LLM agent. Implemented as a Claude Code slash command + hook logic. Reads state.json and routes to the correct subagent.

**Context contract:**
- Reads: `state.json`, `workspace/classifier.md` (for pipeline variant), `check_report.json` (for routing)

**Tools:** File read, File write (state.json only)

**Output:**
```json
// state.json — updated after every stage
{
  "assignment_id": "string",
  "company": "string",
  "assignment_name": "string",
  "current_stage": "string",
  "loop_count": 0,
  "last_checkpoint": "ISO datetime",
  "hitl_nudge_count": 0,
  "status": "active|complete|paused|failed",
  "selected_outputs": [],
  "budget": {
    "complexity": "low|medium|high",
    "estimated_runtime_minutes": 0,
    "approved": true
  }
}
```

**Guardrails:**
- Never increment loop_count for Visual QA → Formatter loops (only Checker → draft loops count)
- Never start Formatter before `check_report.json.verdict == "PASS"`
- Always write checkpoint to state.json before invoking next agent
- After loop_count reaches 2 on FAIL: surface HITL with best draft + unmet criteria; do not auto-loop again

**Failure modes:**
- state.json missing → assume fresh start; prompt user for company/assignment name
- check_report routing loops infinitely → loop_count guard catches this at 2

---

## Agent 1 — Media Analysis Agent

**Responsibility:** Analyze user-provided media files (screenshots, PDFs, recordings) and register them in the company media registry with searchable metadata.

**Model:** Sonnet (vision required; Haiku lacks sufficient visual reasoning for UI flows)

**Context contract:**
- Reads: `INPUT.md` (for assignment context to inform analysis), `MEDIA_REGISTRY.json` (to check if file already registered)
- Does NOT read: workspace/ files, draft.json, Company_Memory.md

**Skills:** None

**Tools:**
- Vision (multimodal) — for screenshots, Figma exports, image files
- PDF text extraction — for PDF files
- File write — `.meta.json`, `MEDIA_REGISTRY.json`, `INPUT.md` (append media refs)

**Output — `.meta.json` per file:**
```json
{
  "id": "string",
  "file": "media/2026-07-05_1430_home_screen.png",
  "timestamp": "ISO datetime",
  "type": "screenshot|pdf|recording|figma|other",
  "platform": "iOS|Android|Web|null",
  "source_company": "string",
  "competitor": false,
  "competitor_name": "string | null",
  "screen_name": "string",
  "flow": "string | null",
  "description": "string (2-3 sentences)",
  "key_elements": ["string"],
  "analysis_summary": "string (detailed — this replaces re-reading the image)",
  "analysis_confidence": "high|medium|low",
  "tokens_used_to_analyze": 0,
  "requires_reanalysis": false,
  "assignments_used_in": []
}
```

**Output — `MEDIA_REGISTRY.json` update (append entry):**
```json
{
  "id": "string",
  "file": "media/filename",
  "meta": "media/filename.meta.json",
  "type": "screenshot|pdf|recording|figma",
  "summary": "one-line description",
  "competitor": false,
  "competitor_name": "string | null",
  "timestamp": "ISO datetime",
  "assignments": []
}
```

**Returns to orchestrator:** `{ "registered": ["id1", "id2"], "status": "complete" }`

**Guardrails:**
- Never overwrite an existing `.meta.json` without checking if file is already registered
- Set `analysis_confidence = "low"` if image is blurry, too small, or ambiguous — do not fabricate detail
- PDF: extract text and structure; do not hallucinate content not present in document
- Mark competitor media explicitly: `competitor: true, competitor_name: "<name>"`

**Failure modes:**
- File not readable → write `.meta.json` with `analysis_confidence: "low"`, `description: "file unreadable"`, `requires_reanalysis: true`
- MEDIA_REGISTRY.json missing → create it fresh with this entry as first item

---

## Agent 2 — Intake Agent

**Responsibility:** Collect the assignment and all supporting inputs, and write them to a structured INPUT.md.

**Model:** Haiku (simple structured writing task; no reasoning required)

**Context contract:**
- Reads: User-provided text (assignment, JD, competitors, constraints — passed as prompt input)
- Does NOT read: workspace/ files, Company_Memory.md, MEDIA_REGISTRY.json

**Skills:** None

**Tools:** File write (INPUT.md only)

**Output — `INPUT.md` structure:**
```markdown
# INPUT

## Assignment
[verbatim assignment text]

## Job Description
[verbatim JD or "Not provided"]

## Interviewer / Hiring Manager
[name, role, LinkedIn if known — or "Not provided"]

## Target Company
[company name]

## Competitors to Reference
[list or "Not specified"]

## Output Format Requirements
[if specified by company — or "Not specified"]

## Deadline
[date/time or "Not specified"]

## Constraints
[budget, page limits, tool restrictions, etc.]

## Media Files
[auto-populated by Media Analysis Agent — list of registered media IDs]

## Notes
[anything else user mentioned]
```

**Returns to orchestrator:** `{ "status": "complete", "input_md_written": true }`

**Guardrails:**
- INPUT.md is immutable after this stage — write it once; never overwrite
- If field is not provided, write "Not provided" — do not fabricate
- Do not add any interpretation or inference — raw collection only

**Failure modes:**
- Assignment text empty → surface HITL: "No assignment text provided. Please paste the assignment."

---

## Agent 3 — Workspace Manager

**Responsibility:** The only agent that writes to workspace/ section files and regenerates WORKSPACE.md as the human-readable merged view.

**Model:** Haiku (structured file writing; no reasoning)

**Context contract:**
- Reads: The specific section content passed to it by other agents (not workspace/ files)
- Always called by other agents via: "Update section X with this content: [content]"

**Skills:** None

**Tools:** File write (workspace/<section>.md, WORKSPACE.md)

**Protocol:**
1. Receive: `{ "section": "research_q1", "content": "markdown string" }`
2. Write: `workspace/research_q1.md` with content
3. Regenerate: `WORKSPACE.md` by stitching all existing workspace/*.md files with headers

**Returns to caller:** `{ "status": "written", "section": "research_q1", "file": "workspace/research_q1.md" }`

**Guardrails:**
- Never read workspace/ files (it only writes them)
- Never summarize or modify content — write exactly what it receives
- WORKSPACE.md stitching order: intent → hiring_signal → classification → context → research_plan → research_* → insights → hypotheses → recommendations → tradeoffs → assumptions → decisions → devils_advocate → executive_review → open_questions → next_steps

**Failure modes:**
- Section file already exists → overwrite (updates are expected)
- workspace/ folder missing → create it, then write

---

## Agent 4 — Hiring Signal Analyzer

**Responsibility:** Determine what the company is actually evaluating in this assignment, beyond the literal question asked.

**Model:** Sonnet (requires PM domain reasoning)

**Context contract:**
- Reads: `INPUT.md`
- Does NOT read: workspace/ files, Company_Memory.md

**Skills:** `hiring-signal-patterns`, `assignment-type-templates`

**Tools:** None (reasoning only — no web search at this stage)

**Output — passed to Workspace Manager → `workspace/hiring_signal.md`:**
```markdown
# Hiring Signal Analysis

## Core Evaluation Areas
- [area 1]: [why this assignment tests it]
- [area 2]: ...

## Company Style Signals
[what the assignment format + JD reveal about company culture, decision-making style]

## Seniority Signals
[what level this assignment is calibrated for based on scope/expectations]

## Format Expectations
[what presentation style the company likely values]

## What NOT to Optimize For
[aspects of the assignment that are red herrings or secondary]

## Confidence
[0.0-1.0 — how confident in this analysis given available inputs]
```

**Returns to orchestrator:** `{ "confidence": 0.85, "hitl_needed": false }`
(If confidence < 0.75 → orchestrator triggers HITL)

**Guardrails:**
- Separate what is explicitly stated vs what is inferred; label inferences
- Do not add research; reason only from INPUT.md content
- Confidence score must reflect actual certainty — do not default to high

**Failure modes:**
- JD not provided → note in analysis; lower confidence; rely on assignment text only
- Interviewer profile not provided → skip seniority signal inference

---

## Agent 5 — Intent Agent

**Responsibility:** Restate the assignment as a precise, unambiguous Intent Contract that all downstream agents use as ground truth.

**Model:** Opus (this is the most important contract in the pipeline; must be exact)

**Context contract:**
- Reads: `workspace/hiring_signal.md`, `INPUT.md`
- Does NOT read: workspace/context.md, workspace/classifier.md (not yet created)

**Skills:** `pm-frameworks`

**Tools:** None

**Output — passed to Workspace Manager → `workspace/intent.md`:**
```markdown
# Intent Contract

## Restated Goal
[precise one-sentence restatement of what this assignment is asking]

## Hiring Signal Alignment
[how the goal connects to what the company is actually testing]

## Success Criteria
- [ ] criterion 1 (verifiable)
- [ ] criterion 2
- [ ] ...

## Audience
[who will read/evaluate this deliverable]

## Scope: In
- [what is included]

## Scope: Out  
- [what is explicitly excluded]

## Required Output Formats
[PPT, DOC, etc. — or "to be selected"]

## Constraints
[page limits, time limits, tool restrictions, etc.]

## Open Questions
[anything ambiguous that HITL should clarify — empty if none]

## Confidence Score
[0.0-1.0]
```

**Returns to orchestrator:** `{ "confidence": 0.88, "hitl_needed": false, "open_questions": [] }`

**Guardrails:**
- Every success criterion must be verifiable — no adjectives ("good", "thorough"); use procedures
- If open_questions is non-empty AND confidence < 0.75 → set hitl_needed: true
- Do not interpret or expand scope beyond what INPUT.md + hiring_signal.md support

**Failure modes:**
- Very low confidence (< 0.5) → hitl_needed: true, open_questions must be non-empty
- HITL confirms/edits → Workspace Manager updates workspace/intent.md with confirmed version

---

## Agent 6 — Classifier Agent

**Responsibility:** Identify the assignment type and output the appropriate pipeline variant (base agents, skips, emphasis flags, complexity estimate).

**Model:** Haiku (classification task; template lookup)

**Context contract:**
- Reads: `workspace/intent.md`, `workspace/hiring_signal.md`

**Skills:** `assignment-type-templates`

**Tools:** None

**Output — passed to Workspace Manager → `workspace/classifier.md`:**
```markdown
# Assignment Classification

## Type
[one of: prd|product_teardown|growth_strategy|metrics_analytics|case_study|market_research|technical_architecture|exec_memo|pricing_strategy|presentation]

## Complexity
[low|medium|high]

## Base Pipeline
[ordered list of agents to run]

## Skip
[agents to skip for this assignment, with reason]

## Emphasis
- case_builder: [specific emphasis instruction if any]
- research_planner: [specific focus if any]

## Estimated Runtime
[~N minutes]

## Estimated Token Tier
[low|medium|high]

## Rationale
[one paragraph explaining this classification]
```

**Returns to orchestrator:**
```json
{
  "type": "product_teardown",
  "complexity": "medium",
  "pipeline": ["hiring_signal", "intent", "context", "research_planner", "research", "synthesis", "case_builder", "devil_advocate", "checker", "exec_review", "formatter"],
  "skip": [],
  "emphasis": { "case_builder": "weight UX analysis heavily given product teardown type" },
  "runtime_estimate_minutes": 20,
  "token_tier": "medium"
}
```

**Guardrails:**
- Must output one of the 10 defined types — no custom types at MVP
- Skip decisions must be based on complexity + assignment type, not random
- Emphasis instructions must be specific, not vague ("weight X" not "consider X")

**Failure modes:**
- Assignment doesn't clearly map to one type → pick closest; set complexity = high; add note in rationale

---

## Agent 7 — Context Builder Agent

**Responsibility:** Build comprehensive company/product/interviewer context using Company Memory and targeted web research, before any research agents run.

**Model:** Sonnet

**Context contract:**
- Reads: `Company_Memory.md` (freshness check), `INPUT.md`, `workspace/classifier.md`, `MEDIA_REGISTRY.json` (for existing visual context)
- Does NOT read: workspace/intent.md (not needed), workspace/research_*.md (not yet created)

**Skills:** `research-heuristics`

**Tools:** Web search, Web fetch, MEDIA_REGISTRY.json read

**Output — passed to Workspace Manager → `workspace/context.md`:**
```markdown
# Context

## Company Overview
[business model, products, target market, revenue model — with sources + confidence + last_verified date]

## Key Products
[list with brief description each]

## Competitors
[list with brief positioning note each]

## Interviewer Profile
[role, background, known preferences — or "Not available"]

## Recent Developments
[last 3-6 months of relevant news, launches, strategy shifts]

## Known Metrics
[any public metrics — MAU, revenue, growth — with sources]

## Market Position
[brief assessment]

## Constraints Known
[from assignment + company context]

## Freshness Notes
[which fields were refreshed vs reused from Company Memory]
```

**Returns to orchestrator:** `{ "status": "complete", "fields_refreshed": ["competitors", "recent_developments"], "fields_reused": ["business_model", "products"] }`

**Also updates:** `Company_Memory.md` — append new stable facts with `last_verified` date

**Freshness rules:**

| Field | Max age before refresh |
|---|---|
| Business model | 6 months |
| Leadership | 1 month |
| Product UI / flows | 2 weeks |
| Pricing | 2 weeks |
| Competitors | 1 month |
| App reviews | Always fresh |
| Recent news | Always fresh |

**Guardrails:**
- Always label source and last_verified date for each field
- Mark low-confidence fields explicitly
- Never fabricate metrics — if not found, state "not publicly available"
- Prefer screenshots/media analysis over web-scraped UI descriptions

**Failure modes:**
- Company not findable → note in context; proceed with what's available from INPUT.md
- Company Memory missing → create fresh; do full research

---

## Agent 8 — Research Planner

**Responsibility:** Decompose the Intent Contract into a structured research plan with questions, sources, effort levels, parallelization flags, and success criteria.

**Model:** Opus (planning is the highest-leverage reasoning task)

**Context contract:**
- Reads: `workspace/intent.md`, `workspace/context.md`, `workspace/hiring_signal.md`
- Does NOT read: workspace/research_*.md (not yet created), draft.json

**Skills:** `research-heuristics`, `pm-frameworks`

**Tools:** None (planning only — no research at this stage)

**Output — passed to Workspace Manager → `workspace/research_plan.md`:**
```markdown
# Research Plan

## Question List

### Q1: [question]
- Objective: [what finding here enables downstream]
- Sources to hit: [specific sites, types of sources]
- Effort level: simple|comparison|complex
- Can parallelize: yes|no
- Depends on: [Q_id or "none"]
- Success criteria: [what "done" looks like for this question]

### Q2: ...

## Parallelization Map
[which questions run concurrently — group by dependency chain]

## Topic Ownership
[explicitly: Q1 owns "competitor UX", Q2 owns "user reviews", Q3 owns "market metrics" — no overlap]

## Total Estimated Searches
[N]

## Research Depth
standard|deep
```

**Returns to orchestrator:**
```json
{
  "questions": ["q1", "q2", "q3", "q4"],
  "parallel_groups": [["q1", "q2"], ["q3"], ["q4"]],
  "total_searches_estimate": 12,
  "depth": "standard"
}
```

**Guardrails:**
- Topic ownership must be non-overlapping — explicitly state ownership boundaries per question
- Effort levels: simple = 1 agent, 3-10 calls; comparison = 2-4 subagents; complex = 10+ calls
- Do not plan research for facts already available in workspace/context.md — check first

**Failure modes:**
- Intent contract is vague → note in plan; plan for broader coverage; flag open questions

---

## Agent 9 — Research Executor

**Responsibility:** Execute one bounded research question, write findings to the assigned workspace file. (One instance per question; N run in parallel.)

**Model:** Sonnet (standard questions) / Haiku (simple fact lookup)

**Context contract (per instance):**
- Reads: Its specific question from `workspace/research_plan.md` (one question block only)
- Reads: `workspace/context.md` (company background — to avoid re-researching known facts)
- Reads: `MEDIA_REGISTRY.json` → relevant `.meta.json` files (for visual context)
- Does NOT read: other research questions, workspace/intent.md, workspace/synthesis.md

**Skills:** `research-heuristics`

**Tools:** Web search, Web fetch, Vision (if media relevant to question), MEDIA_REGISTRY.json read

**Media routing logic:**
1. Read MEDIA_REGISTRY.json → filter by relevance to question
2. Read `.meta.json` for matches
3. If `analysis_confidence == "high"` AND question answerable from `analysis_summary` → use summary (no image tokens)
4. Else → load image → re-analyze with vision → update `.meta.json`

**Output — passed to Workspace Manager → `workspace/research_<qid>.md`:**
```markdown
# Research: [Q_id] — [question]

## Findings

### Finding 1
- Claim: [specific finding]
- Source: [URL or "Company Memory" or "Media: filename"]
- Source type: web|media|memory|assumption
- Confidence: 0.0-1.0
- Date: [when sourced]
- Quote: [verbatim if available]

### Finding 2...

## Gaps
[what this question could not answer; what would require more research]

## Overall Confidence
[0.0-1.0 for this entire question]

## Recommendation
sufficient|needs_more_research
```

**Returns to orchestrator:** `{ "question_id": "q1", "status": "complete", "confidence": 0.82, "gaps": ["user retention metrics not public"] }`

**Guardrails:**
- Strict topic ownership — only research what's assigned; do not expand scope
- Label every claim with source and confidence — no unsourced statements
- If media analysis_confidence is "low" for relevant images → flag in gaps
- Max searches per question: simple=10, comparison=20, complex=30 — stop and report if limit reached

**Failure modes:**
- Web search returns nothing useful → write gaps, set confidence low, recommend: needs_more_research
- URL unreachable → note, try alternative source, do not fabricate

---

## Agent 10 — Insight Synthesizer

**Responsibility:** Compress all research findings into meaningful business insights — patterns, implications, and "so what" — with conflict flagging.

**Model:** Sonnet

**Context contract:**
- Reads: `workspace/research_*.md` (all research files), `workspace/context.md`
- Does NOT read: workspace/intent.md, workspace/hiring_signal.md, draft.json

**Skills:** `pm-frameworks`

**Tools:** File read (multiple workspace/ files)

**Output — passed to Workspace Manager → `workspace/synthesis.md`:**
```markdown
# Insights

## Insight List

### I1: [insight headline]
- Insight: [what the pattern reveals]
- Pattern: [the underlying data pattern]
- Implication: [what this means for the recommendation]
- Supporting evidence: [Q_id references]
- Contradicting evidence: [Q_id references if any]
- Confidence: 0.0-1.0

### I2: ...

## Conflicts
[where research findings contradict each other]
### Conflict 1
- Tension: [what contradicts what]
- Evidence A: [source]
- Evidence B: [source]
- Proposed resolution: [or "unresolved — flag as assumption"]

## Coverage Check
[which Intent Contract success criteria are now well-evidenced vs still weak]
```

**Returns to orchestrator:** `{ "status": "complete", "insights_count": 7, "conflicts": 2, "weak_criteria": ["criterion_3"] }`

**Guardrails:**
- Do not fabricate insights not grounded in findings
- Every insight must link to at least one Q_id
- Flag conflicts rather than silently picking one side
- Coverage check must explicitly map to workspace/intent.md success criteria

**Failure modes:**
- Research quality is poor across the board → produce what's available; flag all weak criteria; orchestrator surfaces this to user before Case Builder runs

---

## Agent 11 — Case Builder

**Responsibility:** Build the recommendation, argument, story, and structured draft — the single source of truth for all output formats.

**Model:** Sonnet

**Context contract:**
- Reads: `workspace/synthesis.md`, `workspace/intent.md`, `workspace/context.md`, `workspace/hiring_signal.md`, `workspace/classifier.md` (for emphasis flags)
- Does NOT read: workspace/research_*.md (synthesis already done), draft.json (this is creating it)

**Skills:** `pm-frameworks`, `writing-style`, `presentation-style`, `hiring-signal-patterns`

**Tools:** None

**Output — `draft.json` (written directly, not via Workspace Manager):**
```json
{
  "title": "string",
  "audience": "string",
  "assignment_type": "string",
  "sections": [
    {
      "id": "s1",
      "type": "executive_summary|problem|insight|recommendation|prioritization|metrics|risks|tradeoffs",
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
  "appendix_sections": [
    {
      "id": "a1",
      "type": "supporting_data|methodology|alternatives|research_citations|assumptions_detail|competitor_analysis|framework_detail",
      "heading": "string",
      "content": "string",
      "supporting_data": ["string"],
      "citations": [
        { "claim": "string", "source": "string", "url": "string | null" }
      ],
      "slide_notes": "string | null"
    }
  ],
  "assumptions_register": [
    {
      "assumption": "string",
      "rationale": "string",
      "confidence": 0.0,
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

**Also writes via Workspace Manager:**
- `workspace/recommendations.md` — recommendation summary for Devil's Advocate and Exec Review
- `workspace/assumptions.md` — human-readable assumptions list
- `workspace/tradeoffs.md` — tradeoffs considered

**Returns to orchestrator:** `{ "status": "complete", "draft_written": true, "assumption_count": 5, "section_count": 8 }`

**Guardrails:**
- Every citation field must be populated — no empty citations
- Every section must map to at least one Intent Contract success criterion
- Apply emphasis flags from workspace/classifier.md (e.g., "weight UX analysis heavily")
- Ungrounded claims → add to assumptions_register with `source_type: "ungrounded"`
- Do not optimize for length — optimize for hiring signal coverage first

**Failure modes:**
- insights.md has too many conflicts → build best case; flag all unresolved conflicts in assumptions_register
- Emphasis flag points to a topic with weak research → note in assumptions; do not fabricate

---

## Agent 12 — Devil's Advocate

**Responsibility:** Challenge the draft recommendation from the perspective of what an interviewer would push back on — without access to how the draft was built.

**Model:** Sonnet (fresh context — NOT the same session as Case Builder)

**Context contract:**
- Reads: `workspace/recommendations.md`, `workspace/assumptions.md`, `workspace/synthesis.md`, `workspace/intent.md`
- Does NOT read: draft.json, workspace/context.md, workspace/research_*.md

**Skills:** `pm-frameworks`, `hiring-signal-patterns`

**Tools:** None

**Output — passed to Workspace Manager → `workspace/devils_advocate.md`:**
```markdown
# Devil's Advocate Report

## Challenges to Recommendation
### Challenge 1
- Issue: [what's weak or missing]
- Likely interviewer question: [exact likely pushback]
- Severity: high|medium|low
- Suggested fix: [specific improvement]

## Missing Tradeoffs
[tradeoffs the recommendation ignores]

## Weak Assumptions
[assumptions most likely to be challenged in interview]

## Counterarguments Not Addressed
[strong counterarguments not pre-empted in recommendation]

## What Would Make This Stronger
[top 3 specific improvements]
```

**Protocol after this agent:**
- Case Builder runs ONE revision pass on draft.json based on this report
- Case Builder revises only the sections flagged; does not rewrite entire draft

**Returns to orchestrator:** `{ "status": "complete", "high_severity_count": 2, "revision_areas": ["section_s3", "section_s5"] }`

**Guardrails:**
- One pass only — Devil's Advocate does NOT loop
- Fresh context only — do not carry over Case Builder reasoning
- Challenge from interviewer perspective, not general quality review

**Failure modes:**
- Recommendations are strong and no major challenges → write short report; state "recommendation is well-constructed"; this is a valid outcome

---

## Agent 13 — Strict Checker

**Responsibility:** Score the draft against the Intent Contract using decomposed binary criteria; route failures to the correct stage; never let a failing draft proceed.

**Model:** Opus (must be different from / stronger than Case Builder; fresh context)

**Context contract:**
- Reads: `draft.json`, `workspace/intent.md`, `workspace/assumptions.md`, `workspace/research_*.md` (for grounding checks), `workspace/hiring_signal.md`
- Does NOT read: workspace/recommendations.md, workspace/devils_advocate.md, workspace/context.md

**Skills:** `checker-rubrics`

**Tools:** Regex/grep (Tier 1 deterministic checks), File read

**Output — `check_report.json`:**
```json
{
  "verdict": "PASS|FAIL",
  "loop_number": 1,
  "draft_hash": "string (for loop detection)",
  "tier1": {
    "all_pass": true,
    "checks": [
      {
        "criterion": "required_format_present",
        "verdict": "PASS|FAIL",
        "evidence": "string (what was checked)",
        "deterministic": true
      },
      {
        "criterion": "all_sub_questions_addressed",
        "verdict": "PASS|FAIL",
        "evidence": "Q1: PASS, Q2: PASS, Q3: FAIL (no coverage of retention metrics)",
        "deterministic": true
      },
      {
        "criterion": "all_quantitative_claims_cited",
        "verdict": "PASS|FAIL",
        "evidence": "string",
        "deterministic": true
      },
      {
        "criterion": "no_placeholder_text",
        "verdict": "PASS|FAIL",
        "evidence": "string",
        "deterministic": true
      },
      {
        "criterion": "assumptions_register_present",
        "verdict": "PASS|FAIL",
        "evidence": "string",
        "deterministic": true
      },
      {
        "criterion": "hiring_signals_covered",
        "verdict": "PASS|FAIL",
        "evidence": "string",
        "deterministic": false
      }
    ]
  },
  "tier2": {
    "all_above_threshold": false,
    "threshold": 0.8,
    "scores": [
      { "criterion": "intent_alignment", "score": 0.9, "reasoning": "string", "verdict": "PASS" },
      { "criterion": "completeness", "score": 0.72, "reasoning": "string", "verdict": "FAIL" },
      { "criterion": "grounding_faithfulness", "score": 0.85, "reasoning": "string", "verdict": "PASS" },
      { "criterion": "insight_quality", "score": 0.88, "reasoning": "string", "verdict": "PASS" },
      { "criterion": "internal_consistency", "score": 0.91, "reasoning": "string", "verdict": "PASS" }
    ]
  },
  "tier3": {
    "notes": ["string"]
  },
  "routing": {
    "route_to": "research|case_builder|intake|formatter|null",
    "reason": "string",
    "specific_fix": "string (actionable instruction for the receiving agent)"
  },
  "unmet_criteria": ["string (human-readable list of what failed)"]
}
```

**Returns to orchestrator:** `{ "verdict": "PASS|FAIL", "loop_number": 1, "route_to": "case_builder", "specific_fix": "..." }`

**Routing logic:**
- Missing/weak evidence, unsupported claims → `route_to: "research"`
- Good evidence, poor argument/missed insight → `route_to: "case_builder"`
- Scope mismatch, answering wrong question → `route_to: "intake"` (triggers user re-clarification)
- Format/consistency defects only → `route_to: "formatter"`
- All pass → `route_to: null` (proceed)

**Guardrails:**
- Never give a holistic score — only binary per-criterion verdicts (Tier 1) or graded per-criterion (Tier 2)
- Chain-of-thought reasoning BEFORE each Tier 2 verdict — do not score without reasoning
- Length-neutral instruction in prompt: "concise answers score equal to verbose if equally correct"
- Loop detection: if `draft_hash == previous_draft_hash` → `verdict: "FAIL"`, `route_to: "hitl"`, message: "Draft unchanged from prior attempt — human review required"
- Do not score Tier 2 if any Tier 1 gate fails — FAIL immediately with routing

**Failure modes:**
- loop_number reaches 2 → orchestrator surfaces HITL regardless of verdict
- routing returns "intake" → orchestrator must surface HITL (cannot loop intake silently)

---

## Agent 14 — Executive Reviewer

**Responsibility:** Review the draft from a hiring-manager/executive perspective and provide advisory feedback.

**Model:** Sonnet

**Context contract:**
- Reads: `draft.json`, `workspace/hiring_signal.md`, `workspace/recommendations.md`
- Does NOT read: workspace/research_*.md, check_report.json, workspace/context.md

**Skills:** `hiring-signal-patterns`

**Tools:** None

**Output — passed to Workspace Manager → `workspace/executive_review.md`:**
```markdown
# Executive Review

## Overall Assessment
[approved|needs_revision — advisory only, does not block pipeline]

## Decision Quality
- Decisive: yes|no — [reason]
- Realistic: yes|no — [reason]
- ROI clear: yes|no — [reason]
- Risks addressed: yes|no — [reason]
- Business impact obvious: yes|no — [reason]

## Strengths
- [what works well from an executive perspective]

## Gaps
- [what an executive would want that's missing]

## Feedback
- [specific, actionable notes]
```

**Returns to orchestrator:** `{ "status": "complete", "assessment": "approved|needs_revision", "advisory_only": true }`

**Guardrails:**
- Advisory only — this report surfaces at Final Review for user awareness but does NOT re-route the pipeline
- Evaluate from VP/C-suite perspective, not PM peer perspective
- Do not duplicate Checker findings — focus on strategic/executive lens only

**Failure modes:**
- Draft is very strong → write "approved" with brief strengths. Valid outcome.

---

## Agent 15 — Formatter

**Responsibility:** Render the approved draft.json into the user-selected output format(s). (One instance per format.)

**Model:** Haiku (structured rendering task)

**Context contract:**
- Reads: `draft.json` ONLY
- Does NOT read: workspace/ files, check_report.json, Company_Memory.md

**Skills:** `presentation-style`, `brand-templates`

**Tools:** PptxGenJS (PPTX), docx library (DOCX), HTML renderer

**Output:** `OUTPUTS/<format_file>` (e.g., OUTPUTS/presentation.pptx, OUTPUTS/document.docx)

**Returns to orchestrator:** `{ "format": "pptx", "status": "complete", "file": "OUTPUTS/presentation.pptx" }`

**Guardrails:**
- Only runs on `check_report.json.verdict == "PASS"` — orchestrator enforces this
- All formats render from draft.json — never read WORKSPACE.md or workspace/ files
- Never add content not in draft.json — do not embellish
- Leave no placeholder text in output — if a field is missing from draft, write "N/A" not "[INSERT]"

**Failure modes:**
- draft.json section content too long for slide → truncate with "..." and note in qa_report for user review
- Tool failure (PptxGenJS error) → report error to orchestrator; orchestrator surfaces to user

---

## Agent 16 — Visual QA Agent

**Responsibility:** Bug-hunt the formatted outputs — find visual defects, placeholders, layout issues, and rendering errors.

**Model:** Haiku (fresh subagent; visual inspection task)

**Context contract:**
- Reads: `OUTPUTS/<files>` (rendered output files)
- Does NOT read: draft.json, workspace/ files

**Skills:** None

**Tools:** Vision (render PPTX/DOCX/HTML to images for inspection), Regex/grep (placeholder text search)

**Output — `qa_report.json`:**
```json
{
  "format": "pptx",
  "file": "OUTPUTS/presentation.pptx",
  "verdict": "PASS|FAIL",
  "issues": [
    {
      "location": "Slide 3, title",
      "type": "placeholder|layout|broken_image|branding|wrong_count|other",
      "description": "string",
      "severity": "blocking|minor"
    }
  ],
  "slide_count_actual": 10,
  "slide_count_expected": 10,
  "placeholder_found": false,
  "branding_consistent": true
}
```

**Returns to orchestrator:** `{ "verdict": "PASS|FAIL", "blocking_issues": 0 }`
(If FAIL → Formatter re-runs; not counted as Checker loop)

**Guardrails:**
- Approach as bug hunt — assume issues exist until proven otherwise
- Check every slide/page — do not sample
- Blocking issues: placeholders, broken images, wrong slide count, wrong file format
- Minor issues: slight layout misalignment, font inconsistency — note but do not block

**Failure modes:**
- Cannot render file to images (LibreOffice/Playwright not available) → flag as setup issue; skip visual check; log in qa_report

---

## Skill Files (Reference)

Skills are markdown files in `Global/skills/`. Loaded into agent prompts by orchestrator. Not agents themselves.

| File | Who uses it | Content |
|---|---|---|
| `hiring-signal-patterns.md` | Hiring Signal Analyzer, Devil's Advocate, Exec Reviewer, Case Builder | Known patterns of what companies test at each PM level; company type signals; seniority calibration |
| `assignment-type-templates.md` | Classifier, Research Planner | 10 pipeline templates with base agents, skip rules, emphasis defaults |
| `pm-frameworks.md` | Intent Agent, Research Planner, Insight Synthesizer, Case Builder | JTBD, AARRR, RICE, MECE, Porter's Five Forces, 5 Whys, etc. |
| `writing-style.md` | Case Builder | User's personal voice, structure preferences, what to avoid — USER MUST WRITE THIS |
| `presentation-style.md` | Case Builder, Formatter | Deck structure, executive communication, slide design principles |
| `research-heuristics.md` | Research Planner, Context Builder, Research Executor | Source prioritization, question decomposition, confidence scoring |
| `checker-rubrics.md` | Strict Checker | Binary rubric templates per assignment type; Tier 1/2/3 criteria per type |
| `brand-templates.md` | Formatter | Visual templates, color schemes, font rules |

---

## Open Items in Contracts (to resolve during build)

1. **Confidence threshold for Hiring Signal HITL** — Intent Agent triggers at 0.75; validate on first 5 runs
2. **Checker rubric content** — `checker-rubrics.md` needs actual criteria per assignment type; start with prd, product_teardown, growth_strategy first
3. **Loop detection hash** — hash `draft.json` content excluding metadata.created timestamp
4. **Research Executor concurrency** — test Claude Code limits; start with 3 parallel; increase if stable
5. **Draft.json version on revision** — increment `metadata.version` on each Case Builder revision pass; `metadata.checker_loop` tracks which loop produced this version
