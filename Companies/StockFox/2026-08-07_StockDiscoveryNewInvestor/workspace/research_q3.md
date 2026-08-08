# Research: Q3 — What discovery/browsing behaviors are established leading indicators of paid conversion in metered or freemium research/analytics products?

## Findings

### Finding 1 — Activation events are multi-session value thresholds, not raw usage count
- **Claim:** In consumer subscription apps, the strongest conversion predictors are a specific value milestone spanning *multiple sessions/days*, not total actions taken. Cited client examples: a wellness app's best predictor was "≥2 pieces of content consumed within 14 days" (beat a weekly-usage model); a language-learning app's activation event required completing several lessons across multiple distinct days, not one sitting.
- **Source:** RevenueCat blog, "Activation metrics that actually predict retention in subscription apps" (revenuecat.com/blog/growth/activation-metrics)
- **Source type:** Industry practitioner blog (consumer mobile-subscription infrastructure vendor, real anonymized client examples) — Tier 4/9 per source priority.
- **Confidence:** 0.6 — concrete named examples, but aggregated/anonymized, not raw data.
- **Date:** current per fetch, 2026-08-07.

### Finding 2 — Hitting the metered limit is a signal; exploring beyond baseline is a stronger one
- **Claim:** Freemium conversion-prediction models built from realized purchasers show two top behavioral flags: "users hitting paywalls as they reach usage/data/seat limits" and "trying advanced features beyond baseline use." The recommended method is training the definition on your own converters' pre-conversion behavior rather than assuming a universal metric.
- **Source:** Amplitude blog, "Top 10 Metrics to Measure Freemium and Free Trial Performance"
- **Source type:** Industry analytics-vendor blog. **Confidence:** 0.55. **Date:** 2026-08-07 fetch.

### Finding 3 — Comparable metered stock-research products gate depth-per-item, not just count
- **Claim:** Seeking Alpha's free tier limits to ~1 premium article/month; TipRanks' free tier shows a teaser but locks the full "Smart Score" breakdown behind ~$30/mo Premium — both gate on *depth of one analysis* once a user is already engaged with a specific security, not purely a running count.
- **Source:** Current product pricing/App Store pages (aggregated via search).
- **Source type:** Product/company source (pricing pages), no conversion-rate data attached. **Confidence:** 0.45 — current-state observation, not a study. **Date:** 2026-08-07.

### Finding 4 — Metered-limit size trades engagement against conversion (NYT)
- **Claim:** NYT's metered-paywall research found looser free limits raise reader engagement but lower subscription conversion, and vice versa — leading NYT to a per-reader "Dynamic Meter" (ML-personalized limit) instead of one flat number.
- **Source:** INMA trade reporting + ResearchGate paper summary ("Paying for What Was Free").
- **Source type:** Secondary reporting on a primary academic/ML system, not read in full. **Confidence:** 0.5. **Date:** 2026-08-07.

## Gaps
No published fintech/stock-app-specific conversion-rate study found (Findings 3 is current-state pricing only). No India-specific freemium fintech benchmark located. General-SaaS freemium benchmarks (2–5% freemium conversion, "40–60% never activate") intentionally excluded per business-lens/comparable-product priority.

## Overall Confidence
0.55 (average across findings; two findings ≥0.55, none below 0.45, none reach 0.7+ "strong secondary source" tier).

## Recommendation
sufficient
