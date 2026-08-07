---
name: assignment-type-templates
description: 10 assignment-type templates with case-builder emphasis, optional-stage flags, and success-criteria checklists. Used by research-planner to classify the assignment and by strict-checker for type-specific rubric routing.
---

# Assignment Type Templates

Every assignment runs the same 7-stage pipeline (intake-intent → research-planner → research-executor(s) → case-builder → devils-advocate → strict-checker → formatter). These templates only set **emphasis** for Case Builder and whether the two optional stages apply: Devil's Advocate (default ON, skip only where noted) and Executive Review (default OFF — opt in via `/output-select` when the audience is genuinely executive).

## `prd`
Case Builder emphasis: lead with quantified success metrics; requirements, edge cases, integration considerations, rollout, risks; must-haves vs nice-to-haves separated; engineering-effort aware.
Success checklist: problem statement · measurable metrics · requirements · edge cases · rollout plan · risks · open questions flagged.

## `product_teardown`
Emphasis: lead with an opinionated verdict, not hedged; what works / doesn't / top-3 recs; UX + business-model analysis; end with prioritized recs, not a wishlist.
Checklist: explicit verdict · UX + business model both covered · specific evidence per critique · prioritized recs · competitor comparison where relevant.

## `growth_strategy`
Emphasis: diagnose current state (AARRR leak point) before solutions; highest-leverage lever with evidence; propose experiments not just initiatives; north star metric.
Checklist: diagnosis with evidence · leverage lever identified · experiments proposed · north star defined · prioritization rationale · realistic phasing.

## `metrics_analytics`
Skip Devil's Advocate (diagnostic, not a single recommendation to attack). Emphasis: metrics tree first; ranked hypotheses; data source per hypothesis; instrumentation gaps; next steps.
Checklist: metrics tree · ≥3 ranked hypotheses · data sources identified · root-cause call (even hedged) · next steps defined.

## `case_study`
Emphasis: break the problem into non-overlapping parts that together cover it (structure it, don't name the framework); situation → complication → resolution → recommendation; tradeoffs acknowledged; impact quantified.
Checklist: breakdown is non-overlapping and complete · diagnosis evidenced · options evaluated · clear recommendation · tradeoffs · impact quantified.

## `market_research`
Skip Devil's Advocate (no single recommendation to challenge). Emphasis: TAM/SAM/SOM; differentiated competitive landscape, not a feature list; clear target segment; strategic implication.
Checklist: market size with methodology · structured landscape · differentiation · segment defined · strategic implication.

## `technical_architecture`
Emphasis: scope/constraints first; key components + interactions; scalability/reliability/cost tradeoffs explicit; cross-functional PM lens, not a pure spec.
Checklist: scope defined · components identified · tradeoffs documented · scalability considered · phasing.

## `exec_memo`
Skip Devil's Advocate (format is too brief for a full challenge pass). Emphasis: recommendation in the first paragraph; max conciseness; explicit ask; impact before implementation detail.
Checklist: recommendation stated first · impact quantified · clear ask · MECE logic · 1–2 pages.

## `pricing_strategy`
Emphasis: value metric identification; competitive pricing landscape; WTP estimation; tiered model with rationale; revenue impact modeled.
Checklist: value metric · competitive pricing · segments/WTP · model with rationale · revenue impact · implementation risk.

## `presentation`
Emphasis: narrative arc first; one message per slide; Pyramid structure (see `deck-builder`); slide-count constraint strictly observed.
Checklist: narrative arc · one message/slide · count within constraint · speaker notes · visual hierarchy · strong open/close.

## Adding a new type
Define emphasis + checklist here, and reference it from `checker-rubrics` if it needs type-specific Tier 1/2 additions. No new agent required — the 7-stage pipeline is fixed.
