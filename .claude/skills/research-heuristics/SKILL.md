---
name: research-heuristics
description: How to plan, execute, and evaluate research efficiently — source priority, question decomposition, effort budgets, confidence scoring. Used by research-planner and research-executor.
---

# Research Heuristics

## Source Priority (highest to lowest)
1. Official company sources (IR, filings, blog) 2. Regulatory filings 3. Reputable press 4. Industry reports (Redseer, KPMG, BCG, McKinsey) 5. App store reviews 6. Social media/Reddit/Twitter 7. Product screenshots/media (via MEDIA_REGISTRY) 8. LinkedIn 9. SimilarWeb/App Annie/Sensor Tower 10. Own inference — always mark as assumption with confidence.
Never: random blogs, unattributed Medium posts, data >2 years old for dynamic fields.

## Question Decomposition
Break into independently researchable sub-questions, each with a clear "done" state and a specific source type. Example: "Why is retention lower than competitor X?" → quantitative rates, qualitative churn reasons, comparative product experience, feature-gap analysis, market/demographic context.

## Effort Levels
**Simple** (1 agent, 3–10 searches): single fact lookup, pricing, rating, bio.
**Comparison** (2–4 searches/side): feature or sentiment comparison across 2–3 products.
**Complex** (10+ searches): full competitive landscape, root-cause analysis, market sizing (top-down + bottom-up).

## Confidence Scoring
0.9–1.0 direct official quote, <6mo. 0.7–0.89 strong secondary source. 0.5–0.69 indirect/aggregated. 0.3–0.49 significant inference. <0.3 assumption, no evidence. Label anything <0.5 explicitly as "Assumption."

## When to Stop
Success criteria met, OR effort budget hit, OR marginal searches return duplicates, OR the gap is better served by a labeled assumption than more searching. Never stop from uncertainty alone — flag low confidence instead.

## Media-First Rule
Check `MEDIA_REGISTRY.json` → `.meta.json` before searching the web for UI/UX facts. Use `analysis_summary` directly if `analysis_confidence == "high"` and it answers the question — no image tokens burned. Only re-analyze the actual image for detail the summary lacks.

## Avoiding Duplicate Research
Check your assigned topic boundary in `research_plan.md` and `context.md` (confidence >0.7 there = don't re-search) before searching.

## Common Patterns by Type
Product teardown: app store reviews (last 90d), Glassdoor, Twitter/Reddit complaints, SimilarWeb, competitor apps. Growth strategy: acquisition channels, retention sentiment, competitor moves, unit economics signals. Metrics diagnosis: industry benchmarks, known drivers, user complaints. Market research: TAM data, key players, regulatory environment, whitespace.

## Freshness (max age before refresh)
Revenue/funding 6mo · product features 2wk · leadership 1mo · market share 1yr · user reviews always-fresh (last 90d) · pricing 2wk · competitors 1mo.
