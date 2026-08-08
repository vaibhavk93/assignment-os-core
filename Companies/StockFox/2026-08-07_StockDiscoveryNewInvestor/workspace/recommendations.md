# Recommendations

## Question → section mapping (intent.md success criterion)

| # | Brief question (verbatim) | Primary section | Supporting section(s) |
|---|---|---|---|
| 1 | How should users discover investment opportunities? | S2 — Explore surface overview | S1 |
| 2 | How do we reduce analysis paralysis? | S1 — problem diagnosis | S3 |
| 3 | How do we make discovery engaging instead of intimidating? | S4 — gamify exploring, not trading | S3 |
| 4 | What information should users see before opening a stock? | S3 — card, shown fields | — |
| 5 | What information should intentionally be hidden until later? | S3 — card, hidden fields + regulatory trace | — |
| 6 | How can we encourage exploration while keeping the experience simple? | S2 — compare tray, unmetered browsing | S5 |

All six map to a named section. None left unanswered.

## Ranked recommendations (impact × confidence × effort)

1. **Ship Explore as a browse-first home** (brand-recognition strip + theme rails + compare tray), demote search to secondary. Impact high, confidence high, effort medium. This is the core ask, grounded in choice-overload evidence and a real competitive gap across all 5 named comparables. A new screen, but low-fidelity and content-driven, no new backend beyond the existing Scorecard.
2. **Hold the pre-click card to five disclosed, factual fields.** No composite score, no price target, no ranked peer comparison. Impact high, confidence medium-high, effort low. The most-scored brief question and the clearest regulatory lever in one decision. The regulatory reasoning is solid; the exact item count is a labelled assumption, not a tested number. A card template, not new data.
3. **Gamify exploration signals only, never trading-adjacent ones.** Impact medium-high, confidence high, effort low. Directly answers the regulatory/risk-judgment hiring signal. Three independent evidence types converge here: FCA, SEC, Robinhood settlement. A constraint on what not to build, which is cheaper than the alternative.
4. **Meter at Scorecard-open only; leave browsing and the compare tray free.** Impact medium, confidence medium, effort low. Protects the exploration behavior tied to conversion in comparable products. The evidence is comparable-product pattern, not StockFox's own funnel data (a live-discussion question). A metering-point decision, not new infrastructure.
5. **Primary metric plus a confidence-inflation guardrail routed through the existing confidence score.** Impact medium, confidence medium, effort low. Makes "is Explore working" answerable, and the harm guardrail is a genuine differentiator. Assumes the confidence score is a longitudinal signal, not a one-time quiz (labelled assumption). Instrumentation, not new UI.
6. **Route the compare tray into Confidence Journal, deep-link jargon into the existing lesson library.** Impact low-medium, confidence medium, effort low. A clean integration that avoids duplicated build; uses what's already shipped.
