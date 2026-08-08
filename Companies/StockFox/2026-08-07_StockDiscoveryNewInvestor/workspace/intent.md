# Intent Contract

**CONFIRMED at `/intent-confirm` on 2026-08-07.** This is ground truth for every downstream agent.

Ratified decisions:
1. **Reframe = mechanism, not replacement.** Ship the stock discovery experience as briefed. Decision anxiety / conviction-building is the reasoning that justifies design choices, worth one framing page, never a substitute for the answer.
2. **Loom beta will not be viewed.** Proceeding without it. Consequence is binding: every statement about StockFox's product today is marketing-site inference and must be labelled as such in the deliverable. Never assert a marketing-site feature as observed beta behaviour. Add an explicit assumption covering the risk that a discovery surface already exists in the beta.
3. **Output = self-contained HTML deck + PDF export.**

## Restated Goal

Produce a ≤10-page/slide submission that designs a **stock discovery experience** for a first-time Indian retail investor who wants to invest but has no first candidate in mind — where the experience's terminal action is the user clicking a stock and opening its StockFox Scorecard.

The artifact's real job is two-part: (a) answer the six questions StockFox posed, and (b) survive a live 1:1 defence on Friday/Saturday where the interviewers "review your solution together, understand your thought process, discuss trade-offs." It is a conversation scaffold, not a finished product spec. Every page must be defensible line by line, because every page will be questioned out loud.

## Hiring Signal Alignment

Assignment type is a **case_study / presentation hybrid** (per `assignment-type-templates`): structured breakdown, situation → complication → resolution → recommendation, tradeoffs acknowledged, one message per page, hard page ceiling. It is *not* a PRD and *not* a product teardown — writing either would be answering a different question.

### Stated (verbatim in the brief — treat as scored criteria, not preamble)
1. **Thought process, assumptions, product decisions** — named three times. Assumptions being *visible and labelled* is explicitly requested; unstated assumptions are a documented red flag.
2. **Trade-offs** — named as an agenda item for the final discussion. A decision without a named cost will get probed live.
3. **Concision as a scored signal** — "keep your submission concise… 5–10 pages", "not looking for pixel-perfect designs or lengthy documentation", "evaluating how you think—not how much you produce", "a simple, well-reasoned solution… is far more valuable than an elaborate presentation." Four separate statements. Over-producing is a failure mode here even when the content is strong: it signals inability to prioritise, which is the Senior PM calibration.
4. **Progressive disclosure is the discriminating question.** Three of their six questions are about what to show, what to hide, and how to stay simple while encouraging exploration. The word "intentionally" in "what information should intentionally be hidden until later" is a tell — they want to see the candidate *say no to information* and justify it. Most candidates will answer "how do users find stocks" (build a screener) and skip this entirely.
5. **The JTBD endpoint is fixed:** discover → click a stock → open the Scorecard. The Scorecard is a shipped surface. Discovery must hand off to it.

### Inferred (labelled — not stated by StockFox)
6. **Regulatory constraint literacy is the cheapest available differentiator.** *(High confidence — grounded in the verified fact that the site states StockFox is not a SEBI Registered Analyst.)* A discovery surface that curates or ranks stocks sits one step from implied advice. Any submission with "Top picks for you" designs something StockFox legally cannot ship. Naming this constraint and tracing at least one design decision to it demonstrates the fintech signal (`trust, compliance, activation friction — rigorous, risk-aware`) that a payments-background Senior PM should own better than any other candidate in the pool. Nobody else will do this.
7. **Discovery is the top of the monetisation funnel.** *(High confidence — grounded in "first 3 stock analyses FREE".)* A metered model makes "which 3 stocks does a new user spend their free analyses on" a business question, not just a UX one. Senior PM calibration per `hiring-signal-patterns` is "do they connect product to revenue?" — one line doing this separates a Senior answer from a PM answer. One line, not a page.
8. **The team's instinct is that confidence comes from education.** *(Medium confidence — inferred from legal entity name containing "LEARNING", EdTech concentration in team background (Coursera, Simplilearn, Pearson), and a fully shipped learning layer with "confidence score tracking".)* Discovery that teaches while browsing is likely to land better with these evaluators than pure recommendation UX. Use as a tiebreaker on design direction, not as a claim in the deliverable.
9. **Early-stage startup signals apply** *(Medium confidence — inferred from company stage and two-way final discussion format)*: resourcefulness, speed, opinionated, no fluff. Also: the final discussion invites "questions from both sides," which means arriving with real questions for them is itself scored.
10. **Seniority calibration is anchored, not guessed.** The level "Senior Product Manager" comes from the assignment title. What the role does day-to-day is unknown — no JD was provided. Calibrate to the generic Senior PM bar (strategic thinking, business impact framing, tradeoff navigation) and do not calibrate to StockFox-specific role scope.

### Red herrings — explicitly do not over-invest
| Temptation | Why it's a red herring | Allowance |
|---|---|---|
| Hi-fi Figma / polished visuals | Ruled out verbatim, twice | Low-fi annotated boxes |
| AI systems depth (RAG, hallucination pipeline, vector DB, latency/cost budgets) | Nobody scores a PM's retrieval architecture in a 3–5h discovery-UX brief; eats pages that should hold product judgement | ≤2 lines, and only where it is a *product* constraint (visible citations → trust; answer latency → discovery feel) |
| TAM / market sizing | Not asked | 0 pages |
| Full competitive teardown of the 5 named products | They were named as reference points, not as the assignment | ≤0.5 page, one "so what" line |
| Multiple full persona cards | Right instinct, wrong page budget | 1 paragraph naming the one behaviour that drives the design |
| Long-form PRD (requirements tables, edge cases, NFRs) | Wrong assignment type; signals output-mode over thinking-mode | 0 pages |
| Named frameworks as headings ("JTBD", "MECE", "RICE") | Consultant tell — per `pm-frameworks`: structure with it, never name it | 0 headings |
| Roadmap / phasing / sprint plan | Not asked | ≤1 line |

### Risk flag on the candidate's stance (must be resolved at `/intent-confirm`)
The candidate wants to reframe "stock discovery" → "reducing decision anxiety / how do beginners build conviction." The instinct is well-aimed at the real problem and matches StockFox's own site language ("Turn research paralysis into confident decisions"). **But the brief's deliverable is stated plainly: "Design a stock discovery experience."** A reframe that *replaces* the deliverable reads as answering a different question — a documented failure mode as damaging as the generic-screener answer it is trying to avoid.

**RESOLVED — user ratified 2026-08-07:** accept the stated deliverable and the stated JTBD funnel as given; use decision anxiety / conviction-building as the explanatory mechanism for the design choices, not as a substitute for the design. Ship the discovery surface. The reframe earns its keep in one framing page, not in place of the answer. Title the deliverable as a discovery experience, not as an anxiety thesis.

## Success Criteria

- [ ] Body page/slide count is ≤10, counted excluding cover and appendix. Appendix (if any) is ≤3 pages and the deliverable is complete without it.
- [ ] All six questions posed in Option 2 are answered. A question→page mapping table exists in `workspace/` (not required in the deliverable itself); every one of the six maps to at least one named page.
- [ ] The deliverable contains a screen-level design of a discovery surface (low fidelity acceptable) whose terminal user action is opening a stock's StockFox Scorecard.
- [ ] A named list of ≥3 information elements that are **deliberately withheld** from the pre-Scorecard view appears in the deliverable, each with the stated reason it is withheld.
- [ ] Assumptions appear in a single labelled list of ≥3 items. Each assumption states the condition that would invalidate it.
- [ ] ≥3 major design decisions each state a cost: what got worse, or which alternative was rejected and why. Zero tradeoff rows list only benefits.
- [ ] The non-SEBI-registered constraint is stated explicitly, and ≥1 design decision is traced to it in text (e.g. how stocks are surfaced without constituting a recommendation).
- [ ] A metrics section names exactly one primary metric with its event-level definition (what counts, what does not), plus ≥2 guardrail metrics, ≥1 of which detects user harm rather than product underuse (e.g. unwarranted confidence).
- [ ] ≥2 existing StockFox surfaces are referenced by their actual shipped product names (from the verified list in INPUT.md), with a stated connection to the discovery experience.
- [ ] Zero pages spent on TAM/market sizing. Competitive comparison occupies ≤0.5 page.
- [ ] Zero framework names used as section headings.
- [ ] Every StockFox product fact asserted in the deliverable traces to the assignment text or the verified research block in INPUT.md. Facts sourced from the marketing site are not asserted as beta behaviour (Loom unviewed — see Open Questions).
- [ ] Every competitor claim is attributed to its source. The StockGro "90%" figure, if used at all, is attributed to StockGro.
- [ ] Final format is one of, or a combination of, the formats the brief permits: PRD, user flows, wireframes, Figma, presentation, Notion, prototype.
- [ ] Deliverable contains ≥2 questions directed back at StockFox (the final discussion explicitly invites "questions from both sides"), or these are captured in `workspace/` for the live conversation.

## Audience

**Primary:** StockFox evaluator(s) — identity not provided. Inferred to be founder-level or senior product leadership at an early-stage company, since the final round is a two-way discussion rather than a one-way presentation. Expect short reading time and a live line-by-line probe.

**Secondary:** the candidate himself, in the Friday/Saturday defence. Anything in the deliverable he cannot defend under questioning is a liability, not an asset. This is the operative filter on every inclusion decision.

**Register:** understated credibility, per candidate profile. No overselling, no superlatives, no claimed certainty where an assumption is doing the work.

## Scope: In / Scope: Out

**In**
- Discovery experience design for a first-time Indian retail investor with no first candidate in mind
- Direct answers to all six posed questions
- The show/hide (progressive disclosure) decision, with reasoning
- The handoff from discovery into the existing StockFox Scorecard
- Labelled assumptions, named tradeoffs, success + guardrail metrics
- Fit with StockFox's already-shipped surfaces and its non-SRA regulatory ceiling
- Low-fidelity visualisation of the discovery surface
- One line connecting discovery to the 3-free-analyses metered model

**Out**
- Option 1 of the assignment (not chosen; content not provided)
- Design of the Scorecard itself — the stated JTBD ends at opening it
- Onboarding, KYC, account creation, broker integration, order placement (research-only product, no demat)
- Pricing / paywall design beyond the single line noted above
- AI systems architecture: RAG design, model selection, infra cost, latency budgets
- Market sizing (TAM/SAM/SOM)
- Full competitive teardown of Screener / Tickertape / Trendlyne / StockGro / TradingView
- Go-to-market, acquisition, growth strategy
- High-fidelity visual design, brand, design system
- Engineering estimation, sprint planning, roadmap beyond one line
- Any research beyond INPUT.md content without explicit user approval

## Required Output Formats

**SELECTED: self-contained HTML deck + PDF export.** Single `.html` file openable in any browser with no account, plus a PDF for direct email attachment. Low-fi wireframes rendered in CSS, no image assets.

Binding regardless of selection: ≤10 body pages/slides; low fidelity acceptable and explicitly preferred; format must be openable by the evaluator without a Figma/Notion account unless a public link is used.

Executive Review stage: **off**. The audience is a working product evaluator running a technical discussion, not an executive consuming a memo.

## Constraints

**From the brief**
- ≤10 pages/slides equivalent (their recommendation; treated as a hard ceiling)
- ~3–5 hours of intended effort
- Not pixel-perfect; not lengthy documentation
- AI permitted as a thinking partner; output must reflect the candidate's own judgement — no unedited AI-generated content
- Submission within 48–72 hours of receipt
- Must land the stated JTBD: user clicks a stock and opens its Scorecard

**From verified research (INPUT.md)**
- No buy recommendations, no personalised investment advice — StockFox is not a SEBI Registered Analyst
- Research-only; no demat account; user brings their own broker
- Metered access: first 3 stock analyses free
- Existing surfaces to design around, not replace: Stock Health Scorecard, Confidence Journal, Portfolio Checkup, AI Research Copilot, Forward-Testing Simulator, Competitive Lens, plus the shipped learning layer

**From candidate profile**
- Indian retail market context (native — use it; it is a genuine edge over a generic answer)
- Understated positioning register

## Open Questions

| # | Question | Impact if unresolved |
|---|---|---|
| 1 | ~~Loom beta walkthrough~~ | **CLOSED 2026-08-07 — proceeding without it.** Binding consequence: all "current StockFox" claims are marketing-site inference, labelled as such, never asserted as beta behaviour. Carry an explicit assumption that a discovery surface may already exist in the beta, with its falsifier. |
| 2 | ~~Reframe latitude~~ | **CLOSED 2026-08-07 — mechanism, not replacement.** See resolution above. |
| 3 | Date the assignment was received, and the exact submission deadline within the 48–72h window. Today is Friday 2026-08-07. | **Medium.** Sets working time and whether the Friday/Saturday final discussion is this week or next. |
| 4 | Is a JD available for the Senior PM role? | **Low–Medium.** Level is known from the assignment title; role scope is not. Currently calibrating to the generic Senior PM bar. |
| 5 | Output format preference — deck, wireframes + narrative, or a combination? | **Low.** Deferred to `/output-select` by design; noted here so it is not forgotten. |
| 6 | Interviewer / hiring manager identity. | **Low.** No individual-level calibration possible; generic evaluator assumptions stand. |

## Confidence Score

**0.76**

Reasoning: the brief itself is unusually explicit — chosen option, six named questions, stated JTBD endpoint, page ceiling, effort budget, permitted formats, and an explicit statement of what is being evaluated. Company context is verified and grounded rather than assumed, including the two facts that most shape the answer (non-SRA status, metered model). That supports high confidence on *what is being asked*.

Deductions: (a) the current beta is unseen, so every statement about StockFox's product today rests on marketing-site inference — a real risk for an assignment that must fit an existing surface; (b) the reframe latitude is a genuine intent-level fork the user must decide, not one I can resolve from the input; (c) no JD, so role scope is unknown and seniority calibration is anchored only to the title.

Open questions are non-empty → `hitl_needed: true` independent of the score.
