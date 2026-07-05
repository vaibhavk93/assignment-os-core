# Research Plan
_Written by: Research Planner_
_Date: 2026-07-05_

---

## Coverage Map

| Success Criterion (from intent.md) | Research Questions |
|---|---|
| 1. AI-native solution — NOT a chatbot | Q3 |
| 2. Full journey coverage (discovery → post-booking) | Q1, Q2 |
| 3. Indian customer specificity (3+ pain points) | Q2 |
| 4. Algorithm/personalization layer specified | Q3, Q4 |
| 5. Business case (GMV, moat, market timing) | Q5, Q1 |
| 6. Metrics defined | Q3 (comparable OTA metric patterns feed synthesis) |
| 7. Monitoring framework | Q3 (comparable monitoring patterns feed synthesis) |
| 8. Rollout strategy with rationale | Q6 |
| 9. Funnel changes intl vs domestic | Q1, Q4 |

All 9 criteria covered. All 6 questions map to at least one criterion.

---

## Classifier Priority Questions — Coverage Check

| Priority question (from classifier.md) | Mapped to |
|---|---|
| "What is ixigo's current international travel product gap vs MakeMyTrip?" | Q1 |
| "What are the specific pain points of Indian first-time international travelers?" | Q2 |
| "What does AI-native look like in travel (not chatbot) — Airbnb, Google Travel, Booking.com examples?" | Q3 |
| "What is the India outbound international travel market size and growth?" | Q5 |
| "What are Indian passport holders' top visa anxiety points and corridors?" | Q2 |

All 5 priority questions have coverage — reframed into Q1, Q2 (x2), Q3, Q5.

---

## Research Questions

### Q1: Ixigo current international product vs MakeMyTrip/Cleartrip feature gap
**Full question:** What does Ixigo's current international flight/hotel booking flow look like end-to-end (discovery, search, booking, pre-travel, in-travel), and what specific international-travel features do MakeMyTrip and Cleartrip offer that Ixigo currently lacks (visa assistance, forex tools, itinerary building, destination guides, international-specific personalization)?
**Intent coverage:** Criterion #2 (full journey coverage), #5 (business case/competitive moat), #9 (funnel changes intl vs domestic)
**Source type:** App Store / Play Store listings and screenshots for Ixigo, MakeMyTrip, Cleartrip (current versions); product pages; MEDIA_REGISTRY (ixigo_pdf_001 already has high-confidence journey-stage summary — check first before re-analyzing); tech/travel press on MMT international features
**Effort:** comparison
**Model tag:** standard
**Max searches:** 8
**Done when:** Have a stage-by-stage (5 journey stages) comparison table of Ixigo vs MakeMyTrip/Cleartrip international features, with at least 3 concrete feature gaps identified and sourced.

### Q2: India-specific pain points for first-time international travelers
**Full question:** What are the top documented pain points for Indian outbound international travelers — specifically visa anxiety/process confusion, forex/payment complexity (UPI not working abroad, card decline, dynamic currency conversion confusion), and first-time-traveler trust/safety concerns — and which pain points are most acute for the Bangkok/Dubai/Singapore corridors?
**Intent coverage:** Criterion #2 (journey coverage — discovery/research stage), #3 (India-specific pain points, mandatory ≥3)
**Source type:** App Store / Play Store reviews (Ixigo, MakeMyTrip, Cleartrip — last 90 days, international booking reviews); Reddit (r/IndiaTravel, r/personalfinanceindia threads on forex/visa); travel forums; industry articles on Indian outbound traveler behavior
**Effort:** comparison
**Model tag:** standard
**Max searches:** 8
**Done when:** Have at least 3 distinct, evidenced India-specific pain points (one each for visa, forex/payment, first-timer anxiety) with supporting quotes/data points and corridor-specific notes where available.

### Q3: AI-native (non-chatbot) product patterns in global travel
**Full question:** How do leading global travel/consumer products implement AI as an orchestration/personalization layer rather than a chatbot — specifically Airbnb (AI search/categories), Google Travel (things-to-do personalization, price prediction), Booking.com (AI Trip Planner mechanics beyond chat UI), and any airline/OTA examples of proactive AI (e.g., predictive rebooking, dynamic itinerary re-ranking)? What concrete metrics and monitoring approaches do these products use for AI-personalization features?
**Intent coverage:** Criterion #1 (AI-native, not chatbot — the core evaluation gate), #4 (algorithm/personalization layer), #6 (metrics — comparable patterns), #7 (monitoring framework — comparable patterns)
**Source type:** Company engineering/product blogs (Airbnb Tech Blog, Google Travel product announcements, Booking.com AI product pages), reputable tech press (TechCrunch, The Information, Skift) on AI travel product launches, product teardown articles
**Effort:** complex
**Model tag:** deep
**Max searches:** 15
**Done when:** Have at least 4 concrete non-chatbot AI mechanics documented (e.g., specific ranking/personalization logic, not just "uses AI"), each with a named product example, source, and — where available — a metric/monitoring signal the company uses to evaluate it.

### Q4: Ixigo's current AI/ML implementation depth
**Full question:** Beyond the ChatGPT conversational app (already known), what product-level AI/ML capabilities does Ixigo currently have in search ranking, personalization, price prediction, or recommendation systems? What has management said in earnings calls/investor materials about AI roadmap and the $36.5M AI investment earmarked from the Prosus round?
**Intent coverage:** Criterion #4 (algorithm/personalization layer — need current baseline to propose credible next step), #9 (funnel changes — what's already algorithmic vs manual)
**Source type:** Earnings call transcripts/investor presentations (Q1-Q2 FY26), company tech blog if exists, LinkedIn posts from Ixigo product/eng leadership, press coverage of the $36.5M AI investment
**Effort:** simple
**Model tag:** standard
**Max searches:** 6
**Done when:** Have a clear statement of Ixigo's current AI maturity level in product (not just conversational surface) with at least one direct quote or filing reference on AI investment intent.

### Q5: India outbound international travel market sizing
**Full question:** What is the size (GMV/booking volume) and growth rate of the India outbound international travel market, and specifically the Bangkok/Dubai/Singapore corridors? What share of this market do OTAs (vs offline/direct airline booking) currently capture, and how is that shifting?
**Intent coverage:** Criterion #5 (business case — GMV/market timing argument)
**Source type:** Industry reports (Redseer, KPMG travel reports, IATA/tourism board data for Thailand/UAE/Singapore inbound-from-India stats), Ministry of Civil Aviation / tourism board press releases, OTA industry analyses
**Effort:** comparison
**Model tag:** standard
**Max searches:** 8
**Done when:** Have a market size figure (or credible range) with growth rate for India outbound international travel, plus corridor-level data for at least 2 of the 3 target corridors, with source and confidence noted.

### Q6: Rollout feasibility constraints (regulatory, forex, visa partnerships)
**Full question:** What regulatory, payment/forex (RBI/LRS rules on international spend), or visa-API partnership constraints would affect Ixigo's ability to roll out an AI-native international booking layer quickly in the Bangkok/Dubai/Singapore corridors? Are there existing visa-tech or forex-tech partners (e.g., Atlys, BookMyForex, VFS Global integrations) that competitors or Ixigo already use?
**Intent coverage:** Criterion #8 (rollout strategy with rationale — needs real constraints to justify phasing)
**Source type:** RBI circulars/LRS documentation summaries, fintech/travel-tech press on visa-API and forex partnerships, competitor partnership announcements
**Effort:** simple
**Model tag:** standard
**Max searches:** 6
**Done when:** Have at least 2 concrete feasibility constraints (one regulatory/forex, one visa/partnership) identified with source, sufficient to justify a phased corridor rollout rationale.

---

## Execution Sequence

**Parallel group A** (run simultaneously — independent topics, no dependencies):
- Q1 (Ixigo vs competitor product gap)
- Q2 (India-specific pain points)
- Q3 (Global AI-native patterns)
- Q5 (Market sizing)
- Q6 (Rollout feasibility constraints)

**Sequential:**
- Q4 → benefits from running after Q1 (product gap findings help scope what "current AI implementation" means in context), but not strictly blocking. Can run in Parallel Group A if agent capacity allows; otherwise runs immediately after Q1 completes.

**Recommendation:** Run Q1, Q2, Q3, Q5, Q6 in parallel group A (5 concurrent Research Executor instances). Run Q4 either concurrently (if 6 slots available) or immediately following Q1 — no hard blocking dependency, just thematic ordering for the synthesizer's benefit.

---

## Budget Summary

| Question | Effort | Model | Max Searches |
|---|---|---|---|
| Q1 | comparison | standard | 8 |
| Q2 | comparison | standard | 8 |
| Q3 | complex | deep | 15 |
| Q4 | simple | standard | 6 |
| Q5 | comparison | standard | 8 |
| Q6 | simple | standard | 6 |
| **Total** | | | **51** |

---

## Deferred Questions

The following were considered but cut to stay within the 5-7 question budget. Available for `/research-approve` if the user wants deeper support:

- **Deep-dive on Indian outbound traveler demographics/segmentation (age, income, first-time vs repeat split)** — reason cut: Q2 already captures qualitative pain points; demographic segmentation is a nice-to-have for persona richness but not required by any success criterion. Would upgrade Criterion #3 evidence depth.
- **Detailed technical feasibility of specific algorithm designs (e.g., how a re-ranking model would be trained/deployed)** — reason cut: Intent explicitly deprioritizes "deep technical architecture... PM-level, not engineering spec." Q3 and Q4 provide enough grounding for a PM-level algorithm description.
- **Ixigo Assured (insurance) and ancillary revenue attach-rate benchmarks for international bookings** — reason cut: Interesting for business case richness (Criterion #5) but context.md already has ancillary revenue model at confidence 0.9; incremental value didn't justify a 7th+ question over the higher-priority gaps.
- **Competitor (MMT/Cleartrip) international-specific marketing/positioning claims** — reason cut: Overlaps significantly with Q1's feature-gap research; would be redundant rather than additive.

---
