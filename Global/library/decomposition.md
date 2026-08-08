# Decomposition

Loaded on a trigger match from `INDEX.md`. Structure with these; **never name one in an output** — see `pm-frameworks`.

---

## Cynefin method router — *read before choosing any other method*
**Trigger:** you haven't decided which decomposition method fits.
**Source:** Snowden & Boone, HBR 2007. `peer-reviewed`

Classify the problem first, because the method follows from the class:

| Domain | Nature | Method |
|---|---|---|
| **Clear** | Cause and effect obvious to all | Apply the known best practice; don't decompose |
| **Complicated** | Cause and effect knowable by analysis | **Issue trees, MECE, hypothesis-led** — this is their home |
| **Complex** | Cause and effect only visible in hindsight | **Probe → sense → respond.** Run a small experiment. *Issue trees actively mislead here* — they imply a knowable structure that doesn't exist |
| **Chaotic** | No discernible relationship | Act to stabilise first, analyse later |

**The load-bearing consequence:** most product-discovery and user-behaviour problems are **complex**, not complicated. Reaching for a MECE tree on a complex problem produces a confident, tidy, wrong answer. If you cannot state what evidence would falsify your breakdown, you are in the complex domain and owe an experiment, not a tree.

---

## First-principles rebuild
**Trigger:** the obvious breakdown mirrors how the industry already organises itself.
**Source:** the *test* below is the operational distinction; Fermi/Goldratt-style reduction to necessary quantities. `peer-reviewed`

A MECE tree **partitions the existing solution space** — its branches are inherited categories (channels, segments, cost lines, org units). First-principles decomposition **discards the categories** and rebuilds from invariants that hold regardless of industry:

- physical or regulatory limits
- unit economics and arithmetic identities (things that must sum)
- the actual job the user is hiring the product for
- what must be true for the outcome to occur at all

**The test — apply it every time:**
> If your branches could be swapped for a competitor's org chart, it's MECE, not first principles.

MECE is not wrong; it is a *different* tool. Use it for exhaustive coverage of a known space. Use first principles when the inherited categories are themselves the thing hiding the answer.

---

## Issue tree / MECE / hypothesis-led
**Trigger:** the problem space is known and you need exhaustive, defensible coverage.
**Source:** Minto, *The Pyramid Principle*. `practitioner`

Split so no driver sits in two branches and none sits outside. Test both halves explicitly. Hypothesis-led variant: commit to an answer on day 1, then build the tree that would *disprove* it — cheaper than surveying the whole space.

**Not the default.** Route via Cynefin first.

---

## 5 Whys
**Trigger:** one recurring defect with a single causal chain.
**Source:** Ohno / Toyota Production System. `practitioner`
**Known limit:** fails on multi-cause systems — it forces a linear chain onto branching causation and stops at whichever cause you happened to follow.

---

## Abstraction laddering
**Trigger:** the stated problem feels like the wrong altitude.
**Source:** Hayakawa's ladder; d.school/IDEO practice. `practitioner`
Ask **"why?"** to move up (broader problem), **"how?"** to move down (more concrete). A brief that names a solution ("build a discovery feed") usually needs one rung up before it can be answered honestly.

---

## Inversion
**Trigger:** you want failure modes rather than the success path.
**Source:** Jacobi, via Munger. `practitioner`
Ask what would *guarantee* failure, then design to avoid it. Pairs with pre-mortem in `elimination.md`.

---

## Theory of Constraints
**Trigger:** a throughput problem — a funnel, a pipeline, a delivery process.
**Source:** Goldratt, *The Goal* — five focusing steps. `practitioner`
Only the bottleneck matters. Improvements anywhere else are illusory. Identify → exploit → subordinate everything else → elevate → repeat (the constraint moves).
