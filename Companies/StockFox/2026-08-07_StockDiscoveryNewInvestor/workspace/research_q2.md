# Research: Q2 — What does cognitive-load/financial-literacy research say about how much and what kind of information a novice can process before shutting down?

## Findings

### Finding 1: Working-memory chunk limit (7±2, revised to ~4)
- Claim: Working memory holds ~7±2 discrete "chunks" of information at once (Miller, 1956); Cowan (2001) revises this down to ~4 chunks when there's no time to rehearse — closer to a fast pre-click glance than a studied read.
- Source: G. Miller (1956) "The Magical Number Seven"; Cowan (2001), via Britannica/ScienceDirect secondary summaries.
- Source type: Classic peer-reviewed cognitive psychology (read via secondary summary, not primary text).
- Confidence: 0.75 — extremely well-replicated, but it's a general-cognition finding applied to financial UI by inference, not tested there.
- Date: 1956/2001 (foundational, not a freshness-sensitive field).

### Finding 2: Industry translation — 5-7 metrics/screen
- Claim: Dashboard/UX practice converges on 5-7 (some say 5-9) core KPIs per screen as the practical pre-overload ceiling, explicitly derived from Miller's Law.
- Source: Multiple independent UX/BI blogs (ClearPoint Strategy, UXPin, Improvado).
- Source type: Industry practitioner consensus, not peer-reviewed.
- Confidence: 0.4 — convergent range across sources, but none primary research; a specific "12+ KPIs = 40% lower engagement" stat found in one source has no visible methodology and is explicitly excluded from use here.
- Date: 2025-2026 blog content.

### Finding 3: SEC Plain English Rule — the "which type" half
- Claim: SEC Rule 421(d) (1998) mandates plain-English disclosure — short sentences, everyday language, active voice, tables for complex data, no jargon, no multiple negatives — for prospectus summary/risk sections. No universal numeric grade-level target found despite searching.
- Source: SEC rule text, via FindLaw/Bradshaw Law Group legal summaries.
- Source type: Regulatory rule via secondary legal summary (not read at sec.gov directly this pass).
- Confidence: 0.6.
- Date: 1998, still in force.

### Finding 4: Novices' ceiling is about legibility, not just count
- Claim: Novice investors "may not comprehend many financial quantities reported" and "may have no idea what parameters would be important to track" — confirms the constraint is which metrics are parseable, not only how many.
- Source: Secondary academic-literature synthesis (ResearchGate/Fed-conference abstracts on financial information overload).
- Source type: Secondary summary of academic literature.
- Confidence: 0.45.
- Date: 2026 aggregation; underlying studies undated in summary.

## Gaps
No study located (9 searches, in budget) tests an exact pre-click item count against novice-investor comprehension specifically — this number does not exist in what's findable. The Fed's own "Information Overload" working paper measures overload via aggregate text volume, not a per-item UI count, and yields no usable cutoff. Nielsen Norman Group explicitly declines to prescribe a fixed disclosure-level number, recommending user testing instead — stated here plainly rather than manufactured.

## Overall Confidence
0.55 — solid general cognitive-science number (Miller/Cowan) and a real regulatory plain-language precedent (SEC), but the bridge to "N items on a stock card" is reasoned synthesis, not a directly-tested finding.

## Recommendation
sufficient
