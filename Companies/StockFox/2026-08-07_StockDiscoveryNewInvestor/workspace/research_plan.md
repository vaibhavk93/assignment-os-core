# Research Plan

## Type / Complexity / Emphasis

**Type:** `case_study` / `presentation` hybrid (confirmed in `intent.md`; not `prd`, not `product_teardown`).

**Complexity:** Medium. Single well-scoped deliverable, but hard success criteria (regulatory line traced to a design decision, a guardrail metric that must detect *harm* not just underuse, zero-overlap tradeoffs) push the bar above a typical case_study.

**Emphasis (merged from both templates, per `assignment-type-templates`):**
- Non-overlapping problem breakdown that together covers it (situation → complication → resolution → recommendation) — structure with this, never name it as a framework.
- Tradeoffs stated with a named cost, not benefits-only.
- Diagnosis evidenced before recommendation; impact/metrics quantified where possible.
- Narrative arc first, one message per page/slide, Pyramid structure, slide-count constraint (≤10 body pages) strictly observed.

**Optional-stage flags:** Devil's Advocate stays **ON** — neither `case_study` nor `presentation` is in the skip list, and this deliverable makes a single set of recommendations genuinely worth challenging (per `intent.md`, especially the regulatory-line claim and the withheld-information list). Executive Review stays **OFF** per `intent.md`'s explicit `/output-select` decision.

---

## Question List

### Q1: What behavioral-finance evidence describes how novice retail investors go wrong with stock decisions specifically (not generic decision-making)?
- **Objective:** Identify named, evidenced patterns (overconfidence bias, familiarity bias, herding/FOMO, disposition effect) that describe *how* a first-time investor's confidence becomes miscalibrated — grounding both "how do we reduce analysis paralysis" and the hard success criterion requiring a guardrail metric that detects user harm (e.g., unwarranted confidence), not just product underuse.
- **Sources:** Behavioral-finance literature (overconfidence bias, disposition effect, herding in retail trading); if verifiable, SEBI's own published research on individual investor trading outcomes in India (check before citing — do not assert figures unless found at a primary or clearly-attributed source this pass).
- **Effort:** Comparison (multiple distinct bias types, ~4–6 searches).
- **Parallelizable:** Yes.
- **Success criteria:** 2–3 named, sourced bias patterns specific to retail stock decisions, each with a one-line mechanism description usable to justify a guardrail metric definition. Confidence ≥0.5 per finding or explicitly labeled assumption.
- **Lens:** User.
- **Topic ownership (no overlap with Q4):** Q1 owns *why a user's confidence in a specific stock becomes miscalibrated* (cognitive/decision bias). It does not cover engagement-mechanic design (streaks, rewards, social feed) — that is Q4's exclusively.

### Q2: What does cognitive-load / financial-literacy research say about how much and what kind of information a novice can process before shutting down?
- **Objective:** Ground the single most heavily-weighted discriminator in this assignment — what to show vs. intentionally hide before a stock is opened. Needs evidence on chunking/numeracy thresholds and plain-language vs. jargon comprehension in financial contexts, distinct from Q1's *why bias happens* and distinct from the *number-of-options* question already answered in `context.md` (Iyengar/Huberman/Jiang).
- **Sources:** Cognitive-load and financial-literacy/numeracy research (chunking, working-memory limits applied to financial decision contexts); plain-language/jargon-comprehension studies in financial communication. Explicitly excluded: product-by-product examples from the 5 named comparables (that's the capped ≤0.5-page competitive table already in `context.md` — do not re-open it).
- **Effort:** Comparison (~3–5 searches).
- **Parallelizable:** Yes.
- **Success criteria:** A defensible answer to "how many data points / what framing is a novice's ceiling before a card reads as intimidating rather than inviting" — at least one sourced finding, confidence ≥0.5, usable directly to justify which of the Scorecard's 200+ metrics (or metric categories) qualify as a pre-click teaser vs. must wait for the post-click Scorecard.
- **Lens:** Product.

### Q3: What discovery/browsing behaviors are established leading indicators of paid conversion in metered or freemium research/analytics products?
- **Objective:** Ground the primary-metric definition (must be a leading indicator of value, per North Star Metric guidance in `pm-frameworks`) and the one required line connecting discovery to the 3-free-analyses funnel — without drifting into TAM/market sizing or StockFox's own (non-public) funnel data, both explicitly out of scope.
- **Sources:** PM/growth literature on activation metrics and freemium-to-paid conversion patterns (e.g., "aha moment"/activation-metric frameworks, freemium SaaS or fintech case studies); general behavioral-economics literature on trial/sampling behavior. Explicitly excluded: revenue figures, market sizing, any StockFox-specific unpublished metric.
- **Effort:** Comparison (~3–5 searches).
- **Parallelizable:** Yes.
- **Success criteria:** 1–2 named, evidenced "leading indicator" behavior patterns (e.g., a specific action or exploration threshold correlated with conversion in comparable metered products) usable to justify what the discovery experience's primary metric should actually count. Confidence ≥0.5 or explicit assumption label.
- **Lens:** Business.

### Q4: What does the evidence say about gamification/engagement mechanics in trading and investing apps specifically — both the engagement benefit and the documented risk?
- **Objective:** Directly answers the assignment's own "make discovery engaging instead of intimidating" question, and is deliberately shaped to produce a tradeoff (a required success criterion: ≥3 decisions each stating a cost). StockFox already ships gamification (leaderboards, rewards, streaks) in its learning layer (`Company_Memory.md`) — this question tests whether borrowing that pattern into stock *discovery* (as opposed to stock *education*) carries a different risk profile, since gamifying discovery of a tradable asset is not the same as gamifying a quiz.
- **Sources:** Behavioral-finance / fintech-UX research and reporting on gamification's effect on trading frequency and risk-taking (e.g., studies or credible reporting on gamified trading-app design and retail trading behavior); does not need to be India-specific if a strong general finding exists.
- **Effort:** Comparison (~3–5 searches).
- **Parallelizable:** Yes.
- **Success criteria:** At least one sourced benefit-side finding (what gamification does for engagement/exploration) and at least one sourced risk-side finding (what it can do to trading behavior/quality), each confidence ≥0.5 — the pairing is what makes this usable as a named tradeoff in the deliverable, not just a feature justification.
- **Lens:** User (secondary relevance: product — informs whether/how much of StockFox's existing gamified pattern-language extends into the discovery surface).
- **Topic ownership (no overlap with Q1):** Q4 owns evidence about the *engagement mechanism itself* (streaks, rewards, social proof) and its documented effect on trading behavior/frequency. A finding about generic overconfidence unrelated to gamification design belongs to Q1, not here.

---

## Why not more questions (5–6 range considered and rejected)

Two candidate questions were tested and dropped as duplicative or out of scope, per the MECE check:
- *"Find more first-person beginner-overwhelm quotes"* — already attempted in `context.md` Step 2 to the point of diminishing returns (Reddit fetch is blocked this session; web search returns paraphrases, not quotes). A second parallel pass would hit the identical tool constraint, not a resourcing constraint — re-queuing it wastes a parallel slot rather than earning one. Confidence in the *underlying phenomenon* is already adequate (0.5, convergent across independent sources) for a design-rationale point that gets one paragraph in the deliverable, not a statistics section.
- *"Deeper competitive teardown of the 5 named products"* — explicitly capped at ≤0.5 page by `intent.md`'s red herrings table; `context.md`'s light-touch table already fills that budget. More research here cannot appear in the deliverable, which fails the stated planning discipline.

Four questions was the number that survived contact with "does this earn a place in a ≤10-page deck," not an arbitrary floor.

---

## Lens Coverage

- **Product:** Q2
- **Business:** Q3
- **User:** Q1, Q4

Every lens has ≥1 question. (Existing shipped-surface facts that would otherwise ground "product" further — Scorecard, Confidence Journal, etc. — are already fully answered in `INPUT.md`/`Company_Memory.md` at high confidence and explicitly out of scope to re-research, per this task's instructions.)

## Parallelization Map

```
Group 1 (all 4 run concurrently, no dependencies):
  [Q1, Q2, Q3, Q4]
```

No question depends on another's output. All four can be dispatched to `research-executor` in a single parallel batch.
