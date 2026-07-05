# Tradeoffs
_Written by: Case Builder_

## Tradeoff 1: Feature parity vs. systems-level leapfrog
- **Option A (feature parity):** Copy MakeMyTrip's playbook — build a visa portal, build a forex card, catch up feature-by-feature.
  - Pros: Faster to a recognizable "we have visa help too" story; lower ambiguity; easier to scope.
  - Cons: Copies MMT's least defensible layer (bolted-on third-party integrations via Atlys/TripMoney), permanently chasing a 2-3 month head start; does not address success criterion #1 (AI-native, not chatbot/feature) or #4 (algorithm layer); repeats the industry-wide pattern of shipping visible features instead of invisible ranking value.
- **Option B (systems-level leapfrog):** Make visa-friction, forex-decline-risk, and trust-deficit signals into ranking/personalization inputs in a single AI-orchestrated layer.
  - Pros: Matches the global pattern (Airbnb, Booking.com) where ranking — not features — drives the majority of AI-native value; gives concrete form to Ixigo's own stated "hyper-personalization" pillar; harder for MMT to copy because it requires an equivalent architecture, not just an equivalent partnership.
  - Cons: Slower to a customer-visible "win," more technically ambiguous, requires new measurement discipline Ixigo doesn't currently have.
- **Decision:** Option B. The hiring signal explicitly penalizes feature-parity thinking ("generic UX improvements without specifics" is a named red flag), and the global evidence (Insight 2) is unambiguous that ranking, not features, is where defensible AI-native value sits.

## Tradeoff 2: Launch-fastest (Dubai) vs. launch-where-pain-is-sharpest (Bangkok)
- **Option A (Dubai-first, pure feasibility):** Visa-on-arrival, no partner dependency, 4-6 week MVP — optimizes for engineering ease and lowest execution risk.
  - Pros: Fastest path to validating the full architecture end-to-end; lowest regulatory/partnership risk.
  - Cons: Leaves the most urgent, highest-volume, most news-worthy "why now" story (Bangkok visa shock) for a later phase, weakening the timing argument in the interim.
- **Option B (Bangkok-first, pure urgency):** Lead with the corridor where the pain is acute and dated (Thailand's May 2026 visa-free removal).
  - Pros: Captures the sharpest, most defensible "why now" narrative and the highest-volume corridor (2.13-2.5M annual travelers) while it's still current news.
  - Cons: Requires government API integration (8-12 weeks, slower than Dubai) and risks building the hardest parts of the architecture (intent classifier, re-ranker) in the more complex regulatory environment first.
- **Decision:** Neither in isolation — two parallel tracks. A narrow, fast (4-week) Bangkok visa-alert feature ships immediately using only the proactive trigger system (no partnership or full architecture required), while the full architecture build sequences Dubai-first per feasibility. This decouples "capture the urgent win" from "build the durable architecture" instead of forcing a single rollout order to serve both goals.

## Tradeoff 3: Build vs. partner for visa/forex data
- **Option A (build natively):** Source visa-requirement and e-visa-status data entirely in-house.
  - Pros: Fully proprietary, no dependency on a third party's roadmap or pricing.
  - Cons: Slower — MMT already has a working visa layer via Atlys; building from scratch surrenders the 2-3 month head start advantage further rather than closing it.
- **Option B (partner for data, build the ranking layer):** Negotiate a visa-data partnership (Atlys-style) as a data source, but keep the ranking/personalization model proprietary rather than exposing the partner's product as a standalone bolted-on feature (as MMT does).
  - Pros: Closes the data/timeline gap fast while preserving architectural differentiation — the partner is an input, not the product.
  - Cons: Introduces a dependency on partner data quality/availability and a negotiation timeline outside Ixigo's direct control.
- **Decision:** Option B. This closes the partnership gap without abandoning the systems-level differentiation argument from Tradeoff 1 — the partner's data feeds Ixigo's own ranking model rather than becoming a separate MMT-style feature.

## Tradeoff 4: Personalization depth vs. privacy/trust perception
- **Option A (deep, visible personalization):** Explicitly tell users why they're seeing certain content ("because you're a first-time international traveler...").
  - Pros: Transparent; may build trust if executed well.
  - Cons: Can feel invasive or surveillance-like, especially for a user who has never explicitly searched international travel and suddenly sees Bangkok visa content.
- **Option B (invisible personalization, surfaced as relevance):** Personalization changes what ranks higher, but is never narrated to the user as profiling.
  - Pros: Feels like "the product got smarter" rather than "the product is watching me" — consistent with how Airbnb/Booking.com surface ranking improvements.
  - Cons: Harder to build user trust in the mechanism itself since it's invisible; requires the ranking to be good enough that relevance alone earns trust.
- **Decision:** Option B, with the explicit design principle that personalization should manifest as improved relevance, never as visible behavioral profiling.

## Tradeoff 5: India-specific architecture vs. global reusability
- **Option A (build for global reuse from day one):** Design the intent classifier and re-ranker to generalize across passport types and corridors beyond India-outbound, anticipating Ixigo's broader international ambitions (Trenes.com acquisition, Singapore subsidiary).
  - Pros: Avoids future rework as Ixigo expands beyond India-outbound.
  - Cons: Over-engineers for an unvalidated need, slows the India-outbound build, and risks diluting the India-specificity the hiring signal explicitly rewards.
- **Option B (India-outbound-first, corridor-agnostic components):** Build for India-outbound now, but keep the re-ranker and trigger system's architecture corridor-agnostic in design even though the initial signals are India-specific.
  - Pros: Matches the assignment's explicit scope (India outbound, Bangkok/Dubai/Singapore); defers generalization cost until the India build proves the model.
  - Cons: Some rework likely needed when/if Ixigo expands the architecture to other markets.
- **Decision:** Option B. Scope discipline matters more than premature generalization for this assignment and for Ixigo's near-term roadmap.
