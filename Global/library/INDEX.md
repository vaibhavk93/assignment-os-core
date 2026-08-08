# Reasoning Library — Index

The only file here loaded by default. Every row is one reusable move. **Match on `Trigger`, then load only that row's file** — bodies are never read speculatively.

**Two fields, deliberately separate:**
- `tier` = where it came from. `peer-reviewed` · `practitioner` (widely used, not empirically validated) · `self-derived` (extracted from our own assignments).
- `status` = our evidence for it. `seeded` (in the library, never yet used by us) · `proven` (used, and a `/debrief` confirmed it landed) · `candidate` (proposed by `/retro`, not promoted) · `demoted` (counter-evidence found).

Never cite a `practitioner`-tier item as if it were evidence. Never let a `candidate` into a deliverable.

---

## Decomposition — how to break the problem apart
| Move | Trigger — use when… | tier | status |
|---|---|---|---|
| Cynefin method router | **Read first.** You haven't decided *which* decomposition method fits | peer-reviewed | seeded |
| First-principles rebuild | The obvious breakdown mirrors how the industry already organises itself | peer-reviewed | seeded |
| Issue tree / MECE | Problem space is known and you need exhaustive coverage | practitioner | seeded |
| 5 Whys | One recurring defect with a single causal chain | practitioner | seeded |
| Abstraction laddering | The stated problem feels like the wrong altitude | practitioner | seeded |
| Inversion | You want the failure modes, not the success path | practitioner | seeded |
| Theory of Constraints | Throughput problem — only the bottleneck matters | practitioner | seeded |

→ `decomposition.md`

## Behaviour — why people do or don't act
| Move | Trigger — use when… | tier | status |
|---|---|---|---|
| COM-B | Diagnosing *why* a behaviour isn't happening, before picking a lever | peer-reviewed | seeded |
| Münscher choice-architecture taxonomy | You need the exhaustive menu of nudges, not four memorable ones | peer-reviewed | seeded |
| Fogg B=MAP | The behaviour exists but doesn't fire — find the missing multiplier | practitioner | seeded |
| EAST | Fast design of a single nudge | peer-reviewed | seeded |
| MINDSPACE | Broad audit of influences on a behaviour | peer-reviewed | seeded |
| Cialdini's principles | Persuading toward one discrete conversion moment | practitioner | seeded |
| Named bias set | Explaining an observed funnel anomaly (not generating ideas) | peer-reviewed | seeded |
| Hooked | Designing a habit loop — **ethically loaded, read the warning** | practitioner | seeded |

→ `behaviour.md`

## Elimination — cutting the option set
| Move | Trigger — use when… | tier | status |
|---|---|---|---|
| Conjunctive screening | A constraint is real and **cannot be traded off** (regulatory, latency, budget) | peer-reviewed | seeded |
| Elimination by Aspects | >7 options, weakly differentiated | peer-reviewed | seeded |
| APEASE | You have generated intervention options and must cut them | peer-reviewed | seeded |
| Kano | Cutting features that add cost but not satisfaction | peer-reviewed | seeded |
| MoSCoW — the *Won't* half | Scope must shrink and nobody will say what's dropped | practitioner | seeded |
| Pre-mortem | A plan everyone already agrees with | peer-reviewed | seeded |
| Assumption mapping / RAT | Cut options whose riskiest assumption can't be tested in your timeline | practitioner | seeded |
| CD3 | Sequencing under a fixed team where delay has a cost | practitioner | seeded |

→ `elimination.md`

## Feasibility — can this actually be done
| Move | Trigger — use when… | tier | status |
|---|---|---|---|
| Cagan's four risks | Any product concept, before committing to it | practitioner | seeded |
| Long pole | You need the one thing that sets the timeline | self-derived | seeded |
| Core vs context (build/buy/partner) | Deciding whether to build a capability at all | practitioner | seeded |
| Type-1 / type-2 doors | Deciding how much analysis a decision deserves | practitioner | seeded |
| Working Backwards / PR-FAQ | Testing whether an idea is even articulable as a benefit | practitioner | seeded |

→ `feasibility.md`

## Archetypes — what kind of problem is this
**Two independent axes. Classify on both; do not collapse them** — a metric-drop case is a profitability problem *and* an execution problem at once.

| Axis | Trigger | tier | status |
|---|---|---|---|
| Business-decision type | The brief names a business decision ("should we enter / launch / price / cut") | practitioner | seeded |
| PM-competency type | You need to know which skill the interviewer is scoring | practitioner | seeded |

→ `archetypes.md`
