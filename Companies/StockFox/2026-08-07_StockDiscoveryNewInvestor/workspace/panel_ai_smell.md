# Panel Review — ai_smell

## Verdict
hire with reservations — a fast reader hits two real tells before slide 5, but the assumptions slide reads unmistakably human.

## Challenges

### Challenge 1
- Issue: Slide 2 stacks five distinct empirical claims with precise figures in one bullet list — "+10 options in a 401(k) plan drops enrollment ~1.5–2pp", "~4–7 item working-memory ceiling", "93% of F&O traders lost money FY22–24" — and slide 5 adds "FCA study: Push notifications +11% trade count; points/prizes +12% trade count... +8% risky-product trades", "SEC... RFI 2021-167", "$7.5M settlement with Robinhood; one customer made 12,700+ trades in 6 months." None of the Miller/Cowan working-memory figure, the FCA gamification study, the SEC RFI number, or the Robinhood settlement detail appear in `context.md`, which documents exactly four researched topics (voice/overwhelm, comparables, regulatory line, Iyengar choice-overload). For a stated 3–5 hour effort budget, five additional empirical citations surfaced only in the deliverable, untraceable to any research artifact I was given, is the classic shape of a model backfilling authority rather than a candidate's own recall.
- Likely interviewer question: "Where's the FCA study from, and did you read the actual RFI or just its number?"
- Severity: high
- Suggested fix: cut to the one citation `context.md` actually backs (Iyengar/Huberman/Jiang) and either source the gamification claims properly or state them as the candidate's own reasoning, unlabeled as research.

### Challenge 2
- Issue: The four tradeoff rows on slide 8 are grammatically identical — "[Decision]" / "Cost: X. Rejected: Y. Reason: Z." — repeated verbatim four times with zero structural variation. A person defending this live under time pressure writes trade-offs in whatever order the thought occurred; four rows in lockstep three-clause form is a template, not a memory.
- Likely interviewer question: none directly — but it primes the "did a model draft this section" read before any content question lands.
- Severity: medium
- Suggested fix: vary at least one row's structure or drop the Reason clause where it's implicit.

### Challenge 3
- Issue: `Global/candidate/VOICE.md` explicitly blocklists "escalating rhetoric: 'it's not just X, it's Y'." The deck violates its own voice file twice: slide 1's "Zero-candidate isn't one stall. It's three." and slide 4's "Not a formatting choice—it's regulatory: StockFox is not a SEBI Registered Analyst." Both are near-exact instances of the banned pattern, and the second also uses the dash-splice VOICE.md's own contrast-pair example was written specifically to eliminate ("A score with no visible basis reads as a tip... so we show the basis first" — three short sentences, no dash).
- Likely interviewer question: none — but it's the sentence most likely to make a sharp reader's eyebrow go up mid-deck.
- Severity: medium
- Suggested fix: rewrite both as flat declaratives per the VOICE.md contrast pair the candidate's own file already models.

### Challenge 4
- Issue: Slide 2's stat cluster ("~2.5M NSE investors, ~1.4B trades") sits unsourced inline with no footnote or attribution visible on the slide itself, unlike the comparables table (slide 11) which does carry a confidence line. Selective sourcing — some numbers get a confidence/attribution treatment, others (the highest-drama ones: 93%, $7.5M, 12,700 trades) don't — reads like content assembled from different passes rather than one author holding a consistent citation discipline throughout.
- Likely interviewer question: "Where's 2.5M NSE investors and 93% F&O losses from?"
- Severity: low
- Suggested fix: apply the same footnote/confidence convention slide 11 uses to slides 2 and 5.

## Persona close
Strongest tell: **"Zero-candidate isn't one stall. It's three."** — the exact "it's not X, it's Y" cadence the candidate's own `VOICE.md` was written to ban, appearing on slide one. Strongest proof of human authorship: **"Both guardrails assume Explore-specific instrumentation exists; verify with StockFox's data team before shipping."** — a live admission of an unclosed loop, on a metrics slide, that no confident AI narrator volunteers unprompted.
