# Behaviour

Loaded on a trigger match from `INDEX.md`. Use to explain or change what people actually do. **Diagnose before you design** — COM-B first, mechanics second.

---

## COM-B / Behaviour Change Wheel — *the diagnostic*
**Trigger:** working out *why* a behaviour isn't happening, before choosing any lever.
**Source:** Michie, van Stralen & West 2011, *Implementation Science*. `peer-reviewed` — the strongest-evidenced item in this file.

A behaviour occurs only when three conditions hold:

| | Sub-types | Ask |
|---|---|---|
| **Capability** | physical, psychological | Do they *know how*? Can they hold it in working memory? |
| **Opportunity** | physical, social | Does the environment permit it? Do peers do it? |
| **Motivation** | reflective (beliefs, plans), automatic (habit, emotion) | Do they *want* to — deliberately, or reflexively? |

Nine intervention functions follow from the diagnosis: education, persuasion, incentivisation, coercion, training, restriction, environmental restructuring, modelling, enablement.

**Why this ordering matters:** most product answers jump straight to motivation (incentives, nudges) when the real blocker is capability (they don't understand the metric) or opportunity (the entry point doesn't exist). Diagnosing first is what stops you designing a persuasion fix for a comprehension problem.

**Pairs with APEASE** (`elimination.md`) — COM-B *generates* candidate interventions, APEASE *cuts* them. Use them as a pair or you'll generate a menu and pick by taste.

---

## Münscher choice-architecture taxonomy — *the exhaustive menu*
**Trigger:** you need the full set of available nudges, not the four you remember.
**Source:** Münscher, Vetter & Scheuerle 2016, *Journal of Behavioral Decision Making*. `peer-reviewed`

Nine techniques in three groups:

- **Decision information** — translate information (units, framing); make information visible; provide a social reference point
- **Decision structure** — change defaults; change option-related effort; change range or composition of options; change option consequences
- **Decision assistance** — provide reminders; facilitate commitment

Prefer this over EAST when the task is *generating* options; EAST is for executing one.

---

## Fogg B=MAP
**Trigger:** the behaviour clearly exists but doesn't fire.
**Source:** Fogg, *Tiny Habits* 2019. `practitioner`

**Behaviour = Motivation × Ability × Prompt** — a product, so any zero kills it. Ability decomposes into six scarce resources: time, money, physical effort, brain cycles, social deviance, non-routine-ness.

Most useful as a *fault-finder*: if the behaviour isn't happening, exactly one of the three is usually missing, and prompting is the cheapest to fix.

---

## EAST
**Trigger:** designing one specific nudge, fast.
**Source:** UK Behavioural Insights Team, 2014. `peer-reviewed`
Make it **E**asy, **A**ttractive, **S**ocial, **T**imely.

## MINDSPACE
**Trigger:** broad audit of every influence acting on a behaviour.
**Source:** Dolan et al., Institute for Government / Cabinet Office 2010. `peer-reviewed`
**M**essenger, **I**ncentives, **N**orms, **D**efaults, **S**alience, **P**riming, **A**ffect, **C**ommitments, **E**go.
EAST is its successor — BIT concluded nine was too many to apply reliably. Use MINDSPACE to audit, EAST to build.

---

## Cialdini's principles
**Trigger:** persuading toward one discrete conversion moment.
**Source:** *Influence*; unity added in *Pre-Suasion* 2016. `practitioner`
Reciprocity · commitment/consistency · social proof · authority · liking · scarcity · unity.

---

## Named bias set
**Trigger:** explaining an observed anomaly in real data. **Not** for generating ideas.
`peer-reviewed` individually — but note any "top N biases for product" listicle is `blog`-tier and arbitrary. Cite the study, never the listicle.

| Bias | Canonical source |
|---|---|
| Loss aversion, endowment | Kahneman & Tversky; Thaler |
| Choice overload | Iyengar & Lepper 2000 |
| Default effect | Johnson & Goldstein 2003 |
| Anchoring | Tversky & Kahneman 1974 |
| Peak-end rule | Kahneman 1993 |
| Social proof, commitment/consistency | Cialdini |

---

## Hooked — ⚠️ read the warning
**Trigger:** designing a habit or retention loop.
**Source:** Eyal 2014. `practitioner` — **no empirical validation.**
Trigger (external → internal) → Action → Variable Reward (tribe / hunt / self) → Investment.

**Two warnings, both load-bearing:**
1. It is a model, not a finding. Do not present it as evidence.
2. It is **ethically loaded**, and in regulated or financial products it is a liability rather than an asset. Variable reward attached to a consequential action is the exact mechanism regulators cite when they name gamification as harm. Before reaching for it, check whether the action you're habituating is one the user can lose money on.
