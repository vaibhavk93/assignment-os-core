---
name: checker-rubrics
description: Quality rubrics for the Strict Checker agent — Tier 1 hard gates, Tier 2 graded criteria, and per-assignment-type additions. Read this before scoring any draft.json.
---

# Checker Rubrics

## Universal Rules (all assignment types)

### Tier 1 — Hard Gates (deterministic, all must PASS before Tier 2)
| Check | How to verify | FAIL condition |
|---|---|---|
| Output format present | `draft.json` `assignment_type` + a populated `sections[]` that maps to the formats in `state.json.selected_outputs` | Missing entirely |
| All sub-questions addressed | Map each Q_id to a draft.json section | Any Q_id uncovered |
| Quantitative claims cited | citations[] non-empty per number | Uncited number |
| No placeholder text | grep: TODO, [INSERT], [ADD], lorem, TBD, PLACEHOLDER, XXX | Any match |
| Assumptions register present | non-empty if any section.is_assumption == true | Ungrounded claim, no register entry |
| Hiring signals covered | every core_evaluation_area in intent.md has ≥1 addressing section | Any area uncovered |
| Three-lens analysis | `workspace/lenses.md` covers product, business AND user, with ≥1 tension between them named and resolved | Any lens missing/one-line, or lenses listed with no tension surfaced |
| Problem breakdown holds | The draft's structure splits the problem into non-overlapping parts that together cover it. **MECE is not required** — route by fit (see the Cynefin entry in `Global/library/decomposition.md`). Judge the split, not the method. | A driver sits in two sections, or a plausible driver has no section. Also FAIL if the branches are just the industry's standard org chart relabelled |
| Elimination was real, not rationalised | `workspace/decision.md` records ≥2 alternatives that were live candidates, each killed by a **named hard constraint** — a regulatory ceiling, a capability that does not exist, a budget or timeline floor. Cross-check against `workspace/tradeoffs.md`. A conjunctive screen is pass/fail; a comparative score is not elimination. | Fewer than 2 real alternatives; any option eliminated only comparatively ("less impactful", "lower ROI", "weaker fit"); every eliminated option is a strawman nobody would have proposed; or `decision.md` is absent |
| Decision carries a falsifying test | `decision.md` names a kill test with a signal and a threshold that would make the candidate abandon the decision, and the draft carries it | No test, or a test with no threshold ("run a survey", "talk to users"). A decision that nothing could falsify is a preference |
| PM voice, not consultant voice | grep draft.json for: MECE, three-pronged, workstream, value pool, unlock value, enablement, synergies, holistic, best-in-class, "the organization should" — and for framework names announced in prose | Any match. Naming the framework is a FAIL, not a credit — structure is shown by the breakdown, not the label |
| AI justification resolved (conditional) | Applies **only if** `workspace/ai_justification.md` exists. Every `Critical` issue in it must be either fixed in the draft or explicitly answered in the deck. A recommendation that survives a Critical unaddressed is one a CTO refuses to fund as designed. | Any Critical issue neither fixed nor addressed. `High` and below are advisory — do not fail on them, and do not treat the file's absence as a failure |
| No templated sibling structure | For any set of ≥3 sibling items (tradeoff rows, recommendation blocks, metric definitions, persona cards), check whether every member shares one grammatical skeleton with only nouns swapped. At least one must break the pattern. See `voice-and-brevity` → *Structural uniformity*. | All siblings identical in shape. **Found in the shipped StockFox deck:** four tradeoff rows, each `Cost: X. Rejected: Y. Reason: Z.`, passed every word-level check and still read as a filled template |
| Sourcing convention is uniform | One citation treatment applied to every factual claim of comparable weight. If any slide carries a source or confidence line, all comparable ones do. | Selective sourcing, especially the pattern where checkable numbers are attributed and the dramatic ones are bare. **Found in StockFox:** the comparables table carried a confidence line while "93% of F&O traders lost money" carried nothing |
| Candidate's own voice blocklist | **Read `Global/candidate/VOICE.md` and check the draft against its blocklist directly.** That file is the source of truth; do not rely on the list duplicated here, which drifts. High-frequency offenders to grep first: `it's not just`, `isn't just`, `the real question is`, `at its core`, `fundamentally`, and the `X isn't A. It's B.` cadence (grep `n't ` followed by `. It's`). Also flag em-dash splices of the form `—it's`. | Any match. **This gate exists because it failed once:** the StockFox deck shipped with "Zero-candidate isn't one stall. It's three." on slide 1 and "Not a formatting choice—it's regulatory" on slide 4, both banned by `VOICE.md`, and the Checker passed it because this row did not exist. A deck that violates the candidate's own voice file reads as machine-written to exactly the reader being persuaded |

### Tier 2 — Graded (0.0–1.0, threshold ≥0.8, reason before scoring, never holistic-first)
| Criterion | Scoring guidance |
|---|---|
| Intent alignment | 1.0=exact question answered; 0.8=close; <0.6=misaligned |
| Completeness | covered / total success criteria from intent.md |
| Grounding/faithfulness | sample 5 claims, verify against research_*.md; score = verified/sampled |
| Insight quality | 1.0=every insight has implication; 0.8=most; <0.6=mostly restatement |
| Internal consistency | 1.0=fully consistent; 0.5=minor issues; 0.0=contradictions |
| Readability | Count sentences over 25 words, bullets over 16, core slides over 80 body words (`voice-and-brevity`). 0 violations=1.0; 1=0.8; 2=0.6; ≥3=0.3 |
| Candidate voice | Read `Global/candidate/VOICE.md`. Start 1.0, −0.2 per hit on the `voice-and-brevity` blocklist, −0.2 if the register is off (overselling, self-praise, hedge stacks). Tier 1 already greps the consultant list — do not double-count those hits here |
| Memorability | The recall test in `voice-and-brevity`: one named concept (≤4 words, ≥2 appearances), one hero number (cited), one one-sentence-describable visual. All three=1.0; two=0.6; ≤one=0.2 |

**Length-neutral:** concise+correct ≥ verbose+correct. The three rows above penalize length only where it costs clarity — never score a short draft down for being short.

### Tier 3 — Qualitative (advisory, doesn't block): tone fit for audience, brand/format conventions, slide count vs constraint.

## Per-Type Additions

**prd:** Tier1 +[measurable success metrics, rollout plan, ≥1 risk, requirements present]. Tier2: engineering feasibility awareness, edge case coverage. Missing metrics → route case_builder: "add measurable success metrics to [s_id]".

**product_teardown:** Tier1 +[explicit verdict, ≥1 specific actionable recommendation, evidence per critique]. Tier2: opinionatedness, business-model awareness. Vague verdict → route case_builder: "state explicit verdict in exec summary".

**growth_strategy:** Tier1 +[current-state diagnosis, north star defined, ≥1 experiment (not just initiatives), prioritization rationale]. Tier2: hypothesis quality, lever specificity. No experiments → route case_builder: "convert ≥2 initiatives into testable experiments".

**metrics_analytics:** Tier1 +[metrics tree, ≥3 ranked hypotheses, data sources per hypothesis, next steps]. Tier2: hypothesis precision, instrumentation awareness. Vague hypothesis → route case_builder: "must be testable — not 'users are confused'".

**case_study:** Tier1 +[options evaluated not just one path, tradeoffs acknowledged]. Tier2: structural rigor (is the breakdown genuinely non-overlapping and complete — judge the structure, never reward naming the framework), business impact quantification.

## Loop Detection
`draft.json` hash matches prior attempt → skip re-scoring, output `{verdict: FAIL, routing: {route_to: hitl, reason: "not converging"}}` immediately.

## Checker Independence
Fresh context, model different from/stronger than the drafter, never penalize conciseness, score per-criterion before any overall verdict.
