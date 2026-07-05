# Assignment Memory: Ixigo — InternationalBookingExperience

_Written: 2026-07-05 | Status: Complete — learnings captured post-run_

---

## Assignment Summary

**Type:** Product Strategy Case Study
**Topic:** AI-Native International Travel Booking for Indian customers
**Core ask:** What should Ixigo build to win in international travel using AI?
**Delivered:** `presentation.html` (18 slides, 0–12 core + A1–A5 appendix) + `interview_qa.md`
**Pipeline:** 17 stages complete, Checker loop_count = 1 (PASS on second build)

---

## Key Decisions Made

- Output format: HTML slide deck (primary) + interview_qa.md (secondary) — finalized at /output-select
- Scope: India outbound international travel (Bangkok, Dubai, Singapore corridors)
- Seniority: Senior PM depth (deep analysis, multiple frameworks, tradeoffs acknowledged)
- exec_review skipped: no JD provided to calibrate executive audience

## HITL Overrides

- Advisory nudge sent: confirm output format preference before Case Builder runs
- Intent confirmed at v1 — no edit required

## Assumptions Accepted

- India outbound = primary corridors Bangkok, Dubai, Singapore
- 18 slides appropriate (0 title + 12 core + 5 appendix)
- No JD = Senior PM depth calibration
- GMV multiplier 1.3x/2x/3x range (conservative/base/upside) — base case drives recommendation

---

## What Ixigo Was Actually Testing

**Primary hiring signal:** Strategic product thinking depth — can candidate define "AI-native" beyond chatbot/LLM wrapper?
**Secondary signal:** India market knowledge — ₹/UPI/visa/LRS constraints, corridor-specific nuance
**Tertiary signal:** Business case rigor — GMV logic, not just user empathy framing

---

## Central Thesis (passed Checker)

> Ixigo's stated "hyper-personalization" pillar (Q2 FY26 earnings) needs concrete product form — not a chatbot, but a re-ranking engine that takes India-specific signals (visa eligibility, forex capacity, first-timer trust) as inputs to surface the right destination/hotel/payment method before the user knows to ask.

**Why it worked:**
1. Framed as executing already-stated commitment (easier sell than net-new bet)
2. Grounded in global evidence (Airbnb embeddings = 99% of platform conversions — the AI IS the ranking, not the chat surface)
3. "Why now" anchored in live news: Bangkok visa shock (Thai Cabinet May 19, 2026)
4. Business case as GMV mix shift: convert acquisition advantage → margin advantage (not "spend to compete")

---

## Key Intellectual Corrections (Checker loop caught these)

- **Algorithm framing:** Not "wrong algorithm" → "calibrated for domestic transactional intent, not international exploratory intent"
- **Bangkok urgency:** Proactive notification as AI orchestration (policy change detected → alert users with Bangkok search history), not just a feature flag
- **MMT/Atlys:** "2-3 month structural head start" not proven moat; Atlys may be investment-linked/exclusive — government API path elevated as primary
- **Business case:** GMV multiplier shown as range (1.3x/2x/3x), not point estimate

---

## Devil's Advocate — High-Severity Findings (all addressed)

1. **GMV multiplier unverified** → added sensitivity range; recommendation holds at conservative case
2. **Earnings-call overread** → softened to "most credible interpretation of a vague commitment"; alternative reading acknowledged
3. **Two parallel tracks may be relabeled sequential** → explicit staffing assumption added OR single-track-with-milestone framing

Medium-severity (documented but not fully restructured):
4. **Funnel-diff is inference not audit** → labeled in deck; UX audit flagged as pre-build recommendation
5. **Atlys exclusivity risk** → government API path elevated as primary Thailand path

---

## Research Findings to Reuse (High Confidence)

### India outbound market
- Size: ~$8-12B OTA-addressable, 11.4% CAGR
- Top corridors: Bangkok (2.13-2.5M visitors/yr), Dubai (~2M), Singapore (~1.4M)
- OTA penetration: 35-45% of India international bookings (growing from offline)
- Bangkok visa shock: Thai Cabinet decision May 19, 2026 — visa-on-arrival removed for Indians

### Indian traveler pain points
- Visa anxiety: 73% of first-timers cite visa as #1 worry
- DCC/payment confusion: Indian card decline rate internationally ~18-25%
- First-timer trust: 68% of Indian international travelers first-time on their corridor

### Competitive gap (Ixigo vs MMT)
- Ixigo: no live visa assistance, no forex/DCC guidance, no AI-personalized discovery
- MMT: Atlys (visa), TripMoney (forex card), international itinerary builder
- MMT's features are bolt-ons, not architecture — leapfrog opportunity, not catch-up

### Global AI-native patterns (most important for PM framing)
- Airbnb: embeddings-based ranking = 99% of conversions; chat is optional front-end
- Booking.com: 150 ML models under the chat surface; AUC/NDCG + staged A/B mandatory
- Google Flights/Hopper: price prediction = proven non-chatbot AI pattern
- Delta Concierge: chat-shaped today, proactive = future goal — what NOT to copy at launch

### Ixigo AI current state
- Shipped: ChatGPT conversational app, voice agents (90% of chat AI-resolved)
- NOT shipped: Product-layer personalization, search ranking ML, recommendation engine
- Q2 FY26 management quote: "Hyper-personalization: using deep travel data to deliver predictive, preemptive experiences" — explicitly forward-looking, not current

---

## Rollout Strategy That Passed Checker

**Track 1 (4 weeks):** Bangkok visa-alert notification layer
- Proactive alert to users with Bangkok search history when visa policy changes
- Thailand e-visa government API (open) — not Atlys — as data source

**Track 2 (16 weeks):** Full AI-native international ranking engine
- Phase 1 Dubai: visa-on-arrival, no partnership needed, 4-6 week MVP
- Phase 2 Bangkok: government API integration, 8-12 weeks
- Phase 3 Singapore: agent-mediated path, 12-16 weeks
- Architecture: intent classifier (domestic transactional vs international exploratory) → re-ranker with visa/forex/trust signals → proactive trigger system

---

## Metrics & Monitoring Framework (imported from global best practice)

| Layer | Metric | Type |
|---|---|---|
| Pre-launch | NDCG@10 vs baseline | Offline ranking quality |
| Pre-launch | AUC of intent classifier | Offline classification |
| Phase launch | Conversion lift (A/B, 95% CI) | Online |
| Ongoing | Recommendation drift (weekly) | Operational |
| Business | International GMV per acquired user | Lagging |

**Why externally sourced:** Ixigo has no public A/B testing or drift monitoring — framework adapted from Airbnb/Booking.com/Arize AI.

---

## Formatting

- Brand: `#EC5B24` (Flamingo), `#1B1B1B` (bg), `#FAC8A5` (peach accent)
- Slides: 18 (0 title + 12 core + 5 appendix A1-A5)
- Deployed: `github.com/vaibhavk93/CSAixigo` (commit 55d6970, `main` branch)
- GitHub Pages: needs manual enable by user

---

## Pipeline Retrospective

### What worked
- 6 parallel research executors → all files complete, massive time saving
- Deduplication in Insight Synthesizer caught 4 cross-executor overlaps
- Devil's Advocate before Checker → 3 high-severity issues fixed → Checker PASS loop 1
- Insight 3 (feature gap = pain point whitespace) — only surfaced from combining Q1+Q2+Q3; no single question would have produced it

### What was harder than expected
- Session limit hit with 6 parallel executors simultaneously — system recovered, required re-run on failed Qs
- Algorithm framing easy to over-rotate; "calibrated for wrong intent" correction required Devil's Advocate
- Two-track rollout requires explicit staffing assumption to defend — future multi-track rollouts: include team-sizing upfront

### Reusable patterns for similar PM case studies
- Company has chatbot deployed → always probe whether genuine AI-native or chat UI on rule-based logic
- "Why now" anchor = live, dated market event → single best way to make business case concrete
- GMV multiplier → always stress-test as range (conservative/base/upside), never point estimate
- Rollout sequencing → show you weighed "easiest" vs "most defensible" and chose with explicit rationale
