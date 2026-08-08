# Context

Last updated: 2026-08-07 (research-planner pass)

## Scope note

Company overview, product surfaces, team background, regulatory self-description, business model, and the StockGro/Stoxo competitive threat are **already verified in `INPUT.md`** (supplied 2026-08-07, high confidence, marked as such). They are not re-collected here — see `INPUT.md` "Company research supplied with this input" and "Competitors to Reference" sections as the source of record. This file covers only the four gaps this assignment's research needed closed, plus the standard context fields (marked "not researched" where out of scope per `intent.md`).

Per `intent.md` red herrings table: competitive detail here is deliberately light-touch (earns ≤0.5 deliverable page, not a teardown), and no TAM/AI-architecture/onboarding research was performed (explicitly out of scope).

---

## 1. Beginner Indian retail investor voice — overwhelm, in their own words

**Tool constraint, stated upfront:** direct Reddit (r/IndianStockMarket) access is blocked for this session (fetch tool cannot retrieve reddit.com; web search does not reliably surface exact Reddit comment text — it returns paraphrases or unrelated results). This is a documented limitation of this research pass, not evidence the phenomenon is rare. One real forum quote was recovered from a different, India-specific investing community (ValuePickr); the rest is convergent secondary-source pattern evidence.

- **Verbatim quote (real, primary source):** a poster on ValuePickr's "Beginner Portfolio" thread wrote: *"I got into investing during the COVID period and, like many beginners, started off by following tips from TV and Telegram groups—which didn't end well."* [source: forum.valuepickr.com/t/beginner-portfolio/203075 | confidence 0.55 — genuine verbatim primary quote, but single anecdote, poster identity/date not captured, and it's adjacent to "overwhelm" (describes tip-following failure, not literally "too many stocks") rather than a direct match | last_verified 2026-08-07]
- **Paraphrased pattern (not verbatim):** Tickertape App Store/Play Store review aggregation surfaces a mixed signal — some users call the interface "easy to navigate," others describe a "cluttered interface" and features that are "overwhelming" and "need better organization for ease of use." [source: strike.money Tickertape review aggregator + App Store review search | confidence 0.4 — paraphrased by a secondary aggregator, not independently read verbatim | last_verified 2026-08-07]
- **Attributed regulatory messaging (unconfirmed at primary source):** a SEBI investor-awareness line reported as *"Too many tips, too little knowledge is a recipe for losses"* (attributed to a 2024 SEBI campaign by a secondary blog). [confidence 0.35 — could not verify against a primary SEBI page this session; treat as reported, not confirmed | last_verified 2026-08-07]
- **Explicitly excluded from evidence base:** one SEO content blog (smartinvestingindia.com) illustrates paralysis with a fictional persona ("Every morning, Ravi opens five stock screeners, twelve Telegram channels...") and cites unsourced numbers ("3-5% annual return gap," "2.3 million search results"). The persona is explicitly the blog's own invented device, not a real user, and the stats have no visible methodology. **Do not use either in the deliverable as fact or as a real quote.** [confidence 0.15 | last_verified 2026-08-07]
- **Convergent directional pattern (multiple independent finance-education sources, none primary research):** freefincal.com, gopocket.in, bajajfinserv.in, and others independently describe the same shape of complaint for Indian retail beginners — too much unfiltered information, 5,000+ listed companies with no obvious starting point, contradictory advice across Telegram/YouTube/finfluencer channels. Convergence across independently-run sources raises confidence in the *underlying phenomenon* even though no single source is authoritative. [confidence 0.5 for the pattern itself, not for any specific number | last_verified 2026-08-07]

**Net read:** the specific evidence base is thinner than ideal (a known tool constraint, not a research-effort gap — see `research_plan.md` for why this was not re-queued as a parallel research question), but the direction is consistent across every source type checked: tip-following and channel-hopping, not stock-picking itself, is what beginners describe going wrong. That is a genuinely different design target than "too many stocks to filter" — it argues for the discovery surface competing with Telegram/YouTube tip culture, not just with Screener-style filters.

---

## 2. Named comparables — what a brand-new user sees today (light touch, caps at ≤0.5 deliverable page)

| Product | What a brand-new user sees first, per public site/app info | Source | Confidence |
|---|---|---|---|
| **Screener.in** | A search bar plus a library of 10,000+ community-built "screens" (saved filters); a few are editorially surfaced (e.g. "Bull Cartel" — quarterly-growth momentum; "Magic Formula" — Greenblatt-style value+quality). No personalized feed — the burden is on the user to already know what a "screen" is or to search a company name they already have in mind. | screener.in/screens/, dhanarthi.com guide | 0.6 |
| **Tickertape** | Asset-class-segmented home (stocks / MFs / US stocks / gold / credit), curated pre-built screens per segment, a proprietary "Market Mood Index" sentiment gauge surfaced prominently, thematic "discover" collections. More editorial curation than Screener, still filter/screen-centric. | tickertape.in/blog, strike.money review | 0.55 |
| **Trendlyne** | Screener-first, including a "Red Flag" screener; watchlists; "SmartOptions" tools; insider-trade / "smart money" tracking. Markets itself explicitly against "vibes or influencer advice" — an anti-tip positioning close to StockFox's own. | trendlyne.com, x.com/Trendlyne | 0.5 |
| **StockGro** | Social/gamified home: virtual-money contests, leaderboards, a social feed to follow other users' and experts' portfolios, an intraday momentum screener. Discovery is community/social-proof-driven rather than filter-driven. Runs "Stoxo" (SEBI-registered-analyst-backed AI research arm) as a separate, higher-trust product line — see `INPUT.md`. | inc42.com, stockgro.club | 0.55 |
| **TradingView** | Global-first platform; India experience blends a screener, customizable watchlists, and a public "Ideas" feed users can follow — explicitly likened to an Instagram/Twitter follow model in its own docs. Least beginner-India-specific of the five; built for active/global traders first. | tradingview.com support docs | 0.5 |

**So-what (one line):** all five default a brand-new user to a search bar, a filter/screener panel, or a social feed — none lead with a single, opinionated starting point calibrated to "I have zero first candidate in mind." That gap is the opening a design can name; it is not itself a design decision (that's `case-builder`'s job, not this file's).

---

## 3. Regulatory line for a non-SEBI-registered platform (hard success criterion — must be right, not assumed)

Two distinct SEBI regimes are relevant, plus a newer third layer:

- **SEBI (Research Analysts) Regulations, 2014**, last amended Aug 2024 and Dec 2024 (FAQs issued July 2025). Registration as a Research Analyst is required for anyone issuing buy/sell/hold recommendations, price targets, research reports, or "opinion on securities" (including IPOs) — the definition of "research services" was explicitly broadened in the 2024 amendments, and applies regardless of whether the service is paid. [source: sebi.gov.in regulation text + corroborating legal analysis (taxguru.in) | confidence 0.8 | last_verified 2026-08-07]
- **SEBI (Investment Advisers) Regulations, 2013**, Reg. 2(m). Registration as an Investment Adviser is required for anyone providing personalized investment advice "for consideration" (i.e. paid) to a client. [source: investor.sebi.gov.in, SEBI IA regs | confidence 0.8 | last_verified 2026-08-07]
- **2023–2025 "finfluencer" rules** (SEBI, with exchange/ASCI coordination): unregistered creators/platforms may not make direct or indirect stock recommendations, and may not make explicit or implicit claims about returns or performance. Content framed as "educational" is expected to reference price data that is **at least 3 months old**, specifically to stop live-price "education" from functioning as a disguised tip. SEBI-regulated entities (brokers, RAs, IAs, mutual funds) are separately barred from partnering with unregistered finfluencers. [source: convergent secondary legal/compliance reporting — taxguru.in, moneylife.in, exchange4media.com, legal500.com (5+ independently-run outlets agree) | confidence 0.65 — strong convergence, but not read from a single primary SEBI circular this session | last_verified 2026-08-07]

**Genuine, unresolved ambiguity (flag as an assumption in the deliverable, not as settled law):** no SEBI guidance was found that explicitly rules on whether an objectively-sorted, criteria-disclosed screener or ranking (e.g., "sorted by revenue growth, high to low") itself constitutes a "recommendation" the way an editorial "Top Picks" label would. This is inference territory. [confidence in the ambiguity being genuinely unresolved: 0.6 | last_verified 2026-08-07]

**Reasoned inference (mine, not sourced fact — label as such downstream):** the safer design lane is transparent, user-chosen or clearly-labelled objective sort criteria ("sorted by X"), never framed as "curated for you" or an opaque "best" score. StockFox's paid/metered model plus its own "not an SRA/IA" disclaimer (`INPUT.md`) suggests the existing Scorecard is already built to stay on the informational side of this line — a discovery surface should stay in that same lane rather than open a new, higher-risk one. [confidence 0.4 — explicitly my synthesis, not a citation]

---

## 4. Choice overload / decision paralysis — the one load-bearing finding

**Iyengar, Huberman & Jiang (2003/2004), "How Much Choice is Too Much? Contributions to 401(k) Retirement Plans."** Using Vanguard Center for Retirement Research data across ~800,000 employees in 647 plans, the study found that as the number of fund options offered increases, plan *participation* falls — each additional 10 fund options is associated with a 1.5–2.0 percentage-point drop in enrollment. [source: Columbia Business School faculty research page; Pension Research Council (Wharton); clear.dol.gov (US Dept of Labor evidence clearinghouse) — cross-confirmed across 3+ independent citations including a government research-evidence review body | confidence 0.85 | last_verified 2026-08-07]

**Why this citation over the more famous jam/supermarket study (Iyengar & Lepper 2000):** this one is a financial-choice-overload study, not a grocery one — directly analogous to "how many stocks/options to show a first-time investor," not an analogy borrowed from an unrelated domain. Use this one if the deliverable cites only one choice-overload finding.

**Scope note for `case-builder`:** the finding is about the decision to *engage at all* (enrollment), not about the quality of the eventual choice. That maps cleanly onto "reduce analysis paralysis" and "encourage exploration while staying simple" — it does not, on its own, support claims about post-engagement decision quality or investment outcomes. Don't overextend it.

---

## Standard context fields

- **Interviewer profile:** not publicly available — no name given (`intent.md` Open Question #6, flagged "Low" impact). Not researched this pass; explicitly out of scope to chase per intent.md's own impact rating.
- **Known metrics (StockFox usage/revenue/funding):** not publicly available. Not searched this pass — no signal that new company-metrics research is in scope; the assignment's own metrics section is a design output (primary + guardrail metrics for the *discovery experience*), not a lookup of StockFox's existing numbers.
- **Recent developments:** StockGro's "Stoxo" launch is the one material recent development, already verified in `INPUT.md` and within the 1-month competitor-freshness window (`research-heuristics`) as of 2026-08-07. No new search performed — would be pure duplication.
- **Market position:** see `INPUT.md`. TAM/market-sizing explicitly 0 pages per `intent.md` — not researched.

## Fields intentionally not researched (per `intent.md` scope / red herrings table)
TAM/market sizing · AI systems architecture (RAG/latency/cost) · onboarding/KYC · Scorecard internals · full competitive teardown beyond the ≤0.5-page table above.
