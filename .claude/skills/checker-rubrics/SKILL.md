---
name: checker-rubrics
description: Quality rubrics for the Strict Checker agent — Tier 1 hard gates, Tier 2 graded criteria, and per-assignment-type additions. Read this before scoring any draft.json.
---

# Checker Rubrics

## Universal Rules (all assignment types)

### Tier 1 — Hard Gates (deterministic, all must PASS before Tier 2)
| Check | How to verify | FAIL condition |
|---|---|---|
| Output format present | draft.json format field / OUTPUTS/ | Missing entirely |
| All sub-questions addressed | Map each Q_id to a draft.json section | Any Q_id uncovered |
| Quantitative claims cited | citations[] non-empty per number | Uncited number |
| No placeholder text | grep: TODO, [INSERT], [ADD], lorem, TBD, PLACEHOLDER, XXX | Any match |
| Assumptions register present | non-empty if any section.is_assumption == true | Ungrounded claim, no register entry |
| Hiring signals covered | every core_evaluation_area in intent.md has ≥1 addressing section | Any area uncovered |
| Three-lens analysis | `workspace/lenses.md` covers product, business AND user, with ≥1 tension between them named and resolved | Any lens missing/one-line, or lenses listed with no tension surfaced |

### Tier 2 — Graded (0.0–1.0, threshold ≥0.8, reason before scoring, never holistic-first)
| Criterion | Scoring guidance |
|---|---|
| Intent alignment | 1.0=exact question answered; 0.8=close; <0.6=misaligned |
| Completeness | covered / total success criteria from intent.md |
| Grounding/faithfulness | sample 5 claims, verify against research_*.md; score = verified/sampled |
| Insight quality | 1.0=every insight has implication; 0.8=most; <0.6=mostly restatement |
| Internal consistency | 1.0=fully consistent; 0.5=minor issues; 0.0=contradictions |

**Length-neutral:** concise+correct ≥ verbose+correct.

### Tier 3 — Qualitative (advisory, doesn't block): tone fit for audience, brand/format conventions, slide count vs constraint.

## Per-Type Additions

**prd:** Tier1 +[measurable success metrics, rollout plan, ≥1 risk, requirements present]. Tier2: engineering feasibility awareness, edge case coverage. Missing metrics → route case_builder: "add measurable success metrics to [s_id]".

**product_teardown:** Tier1 +[explicit verdict, ≥1 specific actionable recommendation, evidence per critique]. Tier2: opinionatedness, business-model awareness. Vague verdict → route case_builder: "state explicit verdict in exec summary".

**growth_strategy:** Tier1 +[current-state diagnosis, north star defined, ≥1 experiment (not just initiatives), prioritization rationale]. Tier2: hypothesis quality, lever specificity. No experiments → route case_builder: "convert ≥2 initiatives into testable experiments".

**metrics_analytics:** Tier1 +[metrics tree, ≥3 ranked hypotheses, data sources per hypothesis, next steps]. Tier2: hypothesis precision, instrumentation awareness. Vague hypothesis → route case_builder: "must be testable — not 'users are confused'".

**case_study:** Tier1 +[framework applied explicitly, options evaluated not just one path, tradeoffs acknowledged]. Tier2: framework rigor (MECE), business impact quantification.

## Loop Detection
`draft.json` hash matches prior attempt → skip re-scoring, output `{verdict: FAIL, routing: {route_to: hitl, reason: "not converging"}}` immediately.

## Checker Independence
Fresh context, model different from/stronger than the drafter, never penalize conciseness, score per-criterion before any overall verdict.
