# Decision

## The option set (written before ranking)

Six paths that could genuinely answer "first-time Indian investor, no candidate in mind, must end at a Scorecard."

| # | Option | What would have to be true for this to be right |
|---|---|---|
| **A** | **Thematic collections** — non-evaluative editorial groupings ("companies whose products you buy", "India's cement makers"), user picks one, opens a Scorecard. | Beginners will accept someone else's grouping as a starting point, and a taxonomy of securities reads as a taxonomy rather than as a selection. |
| **B** | **Disclosed-criteria sort** — a screener with the criterion always visible ("sorted by 5-yr revenue growth, high→low"), beginner presets available. | Beginners can pick or interpret a criterion, and objective sorting stays on the informational side of the SEBI line. |
| **C** | **Familiarity-first entry** — the surface asks the user to name companies they already deal with as a customer, maps brand → listed entity, opens that Scorecard. StockFox selects nothing. | A first-time Indian investor can name at least one listed company they have a consumer relationship with, unprompted. |
| **D** | **Question-led guided entry** — 2–3 questions about goal/horizon/interest, routed to a shortlist. | Answering questions is less intimidating than browsing, and a question-derived shortlist is not personalised advice. |
| **E** | **Social discovery** — a feed of what other StockFox users are researching, most-researched-this-week, follow-others. | There is enough user-behaviour liquidity to make the feed non-empty and non-misleading, and aggregate attention is safe to surface. |
| **F** | **Learning-layer-as-discovery** — the shipped 4-min lessons *are* the surface; each lesson ends by pointing at the companies the concept applies to. | Education-led discovery is the strongest fit for this team and its shipped assets, and concept→company handoff is permissible for an unregistered platform. |

D, E and F all had real advocates in the inputs: D is the natural read of "reduce analysis paralysis", E is StockGro's validated commercial model, and F is explicitly flagged in `intent.md` (#8) as the direction most likely to land with an EdTech-heavy team. None of them is a strawman.

## Screen — hard constraints, pass/fail, no scoring

Constraints that cannot be traded off:

- **HC1 — Non-SRA/IA ceiling.** StockFox is neither a Research Analyst nor an Investment Adviser. RA registration is required for buy/sell/hold calls, price targets, or "opinion on securities", and the 2024 amendments broadened *research services* regardless of payment (context.md §3, 0.8). IA registration is required for **personalised** advice **for consideration** — and StockFox charges. Unregistered platforms may not make direct **or indirect** recommendations; "educational" content referencing securities is expected to use price data ≥3 months old (0.65).
- **HC2 — Terminal action is fixed.** The primary loop must end in a Scorecard opening. `intent.md` treats this as given.
- **HC3 — No capability that doesn't exist.** Research-only, no demat, early-stage beta, no published user base.
- **HC4 — Three free analyses.** An option that requires more than three Scorecard opens before it delivers anything is dead on arrival.

### Eliminated

| Option | Killed by | Why it is a gate and not a preference |
|---|---|---|
| **E — Social discovery** | **HC3**, then **HC1** | Cold start is absolute: a metered beta where most users have ≤3 analyses cannot populate "what others are researching" without either faking it or exposing a handful of accounts. StockGro can run this lane *because* it has 35M users — that asset is the option's precondition, and StockFox does not have it. Independently, surfacing aggregate retail attention toward named securities is indirect recommendation under HC1, and Q4-F5 shows that exact flow predicts −4.7% 20-day abnormal returns — the platform would be amplifying a documented harm signal. |
| **D — Question-led guided entry** | **HC1** | In the form that makes it worth building, user answers produce a stock shortlist. Personalised output + paid platform is the Investment Adviser definition, and StockFox holds neither registration. Stripped of personalised output, D is a wizard wrapped around A or C — not a distinct path. Cut as an option, retained as a possible entry animation for whatever survives. |
| **F — Learning-layer-as-discovery** | **HC1**, secondarily **HC2** | "Here is a concept, here are the live-priced companies it applies to" is the precise pattern the ≥3-month-stale-price expectation was written to stop — educational framing that functions as a tip. Its primary loop also terminates in lesson completion, so the Scorecard handoff is bolted on rather than native. **This kill is the fragile one:** it rests on a 0.65-confidence reading of convergent secondary reporting, not a primary circular. If counsel reads that rule narrowly, F returns as the strongest challenger, and it is the option best fitted to this team. Flagged, not buried. |

### Survivors, ranked (impact × confidence × effort)

| Rank | Option | Impact | Confidence | Effort | Note |
|---|---|---|---|---|---|
| 1 | **C** | High — the only path that never asks the user for a criterion and never has StockFox nominate a security | High on the regulatory read (nothing is selected); **low on the behavioural premise** | Medium — a brand→entity dataset, not a model | Ranked first on impact and regulatory clearance, not on confidence |
| 2 | **A** | Medium-high — familiar browse feel, immediate breadth | Medium — every collection membership is a defensible-but-arguable selection by StockFox | High and *recurring* — editorial curation with a permanent maintenance tail | The natural default; loses on who is doing the selecting |
| 3 | **B** | Low for *this* user — asks for the criterion that "no candidate in mind" means they lack (Q2-F4) | Highest regulatory confidence | Lowest | Made beginner-usable via presets, it collapses into A and inherits A's selection problem |

## The decision

**Discovery opens on companies the user already has a consumer relationship with. The user names them; StockFox ranks, scores and nominates nothing pre-Scorecard. Non-evaluative thematic collections are the fallback state for users who name nothing, and the shipped Competitive Lens is the second step outward. No engagement mechanics anywhere in the discovery loop.**

C is the entry state, A is the fallback — the load-bearing choice is which one is the default, because that decides who performs the selection.

**Stated fork, not resolved by desk research:** C-as-default vs A-as-default. The evidence favours C (Q2-F4 on missing criteria; context.md §1 on the tip channel being the real rival — a company you already buy from is the anti-tip anchor), but nothing in Q1–Q4 tests whether a novice will actually name a listed company. That is what the kill test below decides. If it fails, A is the default and the recommendation reverts cleanly.

---

## Kill test

**The riskiest claim is that a first-time investor will name a company at all.** Everything else is downstream of it.

- **Test:** ship the entry as a two-variant card on the existing marketing site — no account, no beta access needed. Variant 1: "Name a company whose products you buy." Variant 2 (control, = option A): three non-evaluative collections. 50 first-time visitors per variant. Runs this week; it is a landing card and a lookup, not a product.
- **Signal:** in-session Scorecard opens, plus (variant 1 only) the share of typed inputs that resolve to a listed Indian entity.
- **Thresholds:**
  - Fewer than **8 of 50** variant-1 visitors name a company that resolves *and* open its Scorecard → **abandon C as the default**, A becomes the entry.
  - More than **30%** of typed inputs resolve to an unlisted entity (Amul, Flipkart, a Jio-as-brand input) → the premise holds but the dataset is the problem, not the design; the dead-end path becomes a first-class screen rather than an error.
  - Variant 1 loses to variant 2 on Scorecard-open rate by any margin → the fork resolves to A. No tie-breaking argument needed.
- **What it does not test:** whether the first Scorecard produces a better decision. Out of reach this week, and out of scope for the brief.

## Long pole

**v1 covers roughly 150 consumer-facing listed names because the brand → listed-entity map does not exist yet.**

It is a content asset, not code, and it cannot be parallelised past a point because the hard cases need a judgement call each: brands whose parent isn't listed in India (Lay's, Pepsi), brands inside a conglomerate where the mapping is technically right and experientially wrong (Jio → Reliance), cooperatives (Amul), private companies a user assumes are listed (Flipkart), and multi-brand parents (Maggi and KitKat both → Nestlé India). Every unhandled case is a dead end on the user's very first interaction, which is the one moment the surface cannot afford to fail.

Nothing else on the path is scarce: the entry screen is a text input and a card grid, and the Scorecard, Competitive Lens and Confidence Journal are already shipped.

## And then what

- **Strongest competitor's response:** StockGro/Stoxo can copy the familiarity entry in a sprint — and then attach a SEBI-registered analyst's view to the company the user named, which StockFox legally cannot. The moat is not the entry mechanic; it is that StockFox's whole surface is built to work without ever selecting a security. Expect the mechanic to be copied and the constraint not to be.
- **Internal precedent:** "we never nominate a security" hardens into a design law. That is the right law for an unregistered platform, and it is a genuine constraint on every future surface — including any personalised alerts, watchlist suggestions, or "stocks like this one" feature. It also becomes the answer to the first thing an acquirer or a regulator asks.
- **What it forecloses:** the obvious next monetisation lever — a recommendation or personalisation engine. Choosing this means the growth story runs through depth per company, not breadth per session, and the team should not later be surprised that session-breadth metrics look flat.

## Load-bearing assumptions (ranked by blast radius)

| # | Assumption | Confidence | What invalidates it | Blast radius |
|---|---|---|---|---|
| 1 | A first-time Indian retail investor can name ≥1 **listed** company they deal with as a customer, unprompted. | 0.55 | The kill test: <8/50 resolve and open. | **Whole recommendation.** C's entry premise; nothing in Q1–Q4 tests it. |
| 2 | Surfacing a company the *user* named, with no ranking or score attached, does not constitute research services or advice for an unregistered paid platform. | 0.65 | Counsel or SEBI guidance reading user-triggered surfacing on a paid platform as covered — the 2024 amendments broadened "research services" and no guidance settles the sorting question (context.md §3). | **Whole recommendation**, and every other option too. If this falls, the product problem is registration, not design. |
| 3 | No discovery surface already exists in the unviewed beta. | 0.5 | Watching the Loom. | **Framing of the entire deliverable** — it would turn a design proposal into a redesign proposal. Cheapest open item in the pack and still open; carry it verbatim as an assumption per `intent.md` decision 2. |
| 4 | Anchoring the first pick on familiarity does not materially worsen the user's eventual outcome versus a curated first pick. | 0.4 | A guardrail showing users' researched set never extends past the first named company, or concentrating in it. | **One tradeoff row and the guardrail metric** — not the recommendation. Low confidence, small blast radius; do not let it drive the design. |
| 5 | Depth on one company converts better than breadth across many in this specific funnel. | 0.5 | Meter-exhaustion rate falling without a matching rise in conversion. | **The primary metric definition**, not the surface design. Q3-F3 is current-state pricing observation, not a study. |

---

## Methods Used

- Cynefin method router (`decomposition.md`) — split the brief into an analysable half (regulatory line, information ceiling) and a probe-first half (what makes a novice click), which is why the recommendation ships with a falsifier instead of a spec — **changed the answer: yes**
- Conjunctive screening (`elimination.md`) — killed E, D and F on named hard constraints before any scoring; without it E and F would have survived on a respectable weighted score — **changed the answer: yes**
- Long pole (`feasibility.md`) — surfaced the brand→entity map as the timeline setter when the build otherwise looked trivially easy — **changed the answer: yes**
- Assumption mapping / RAT (`elimination.md`) — ordered the load-bearing assumptions by blast radius rather than confidence, which is what moved the untested naming premise above the better-evidenced regulatory one — **changed the answer: yes**
- Cagan's four risks (`feasibility.md`) — checked; value/usability/feasibility/viability were already covered by the screen and the three lenses, and it added nothing the constraint screen had not already caught — **changed the answer: no**
- Type-1 / type-2 doors (`feasibility.md`) — read to check whether this decision warranted the analysis depth; the regulatory posture is one-way and the entry screen is two-way, which matches how the work was already split — **changed the answer: no**
- Issue tree / MECE (`decomposition.md`) — considered and not used; the routing put the core question in the probe-first half, where a tree would have manufactured false structure — **changed the answer: no** (used as a rejection, correctly)
