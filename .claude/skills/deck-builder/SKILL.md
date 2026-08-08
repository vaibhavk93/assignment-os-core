---
name: deck-builder
description: Use when structuring or rendering any assignment deliverable — HTML slide deck, PPTX, or DOCX. Covers Pyramid Principle structure, core/appendix split, brand colors, and format-specific rendering rules. Used by Case Builder (structure) and Formatter (rendering).
---

# Deck Builder

One skill governing structure (how the argument is organized) and rendering (how it looks) for every output format. HTML is the default/preferred format; PPTX/DOCX specifics are in `references/pptx-docx.md` — read that file only when the selected output format is pptx or docx.

## Structure (applies to every format)

**Pyramid Principle — answer first.** Recommendation → 3ish arguments → evidence per argument. Never data → analysis → conclusion.

**One message per slide/section.** The heading IS the argument, not a topic label.
- ❌ "Market Analysis" — ✅ "India outbound market is $23–35B growing 11.4% YoY — Ixigo captures <5%"

**Always bifurcated: Core + Appendix.**
- Core (10–12 sections): Executive Summary → Problem framing → Context → Analysis (by sub-topic) → Recommendation → Tradeoffs/risks → Metrics → Roadmap.
- Appendix (no limit): supporting data, methodology, alternatives considered, detailed research, competitive detail, assumptions register.
- Every core slide must earn its place — "useful to have" goes to appendix.

**Executive Summary standalone rule.** If the reader reads only this section, they understand the recommendation: 1-sentence problem, 1-sentence recommendation, 3 supporting bullets, quantified impact.

**Assumptions:** every ungrounded claim is labeled, listed in the assumptions register, and paired with a falsifier ("wrong if conversion is below 3%").

## Brand colors — mandatory first step, every time

Search `[Company] brand colors hex` before writing anything. Never default to generic blue (#007BFF, #1A73E8). Fallback only if search fails: `--color-primary: #E85D04`, `--color-background: #0D1B2A`.

## HTML — self-contained single file

```css
:root {
  --color-primary: [brand color];
  --color-background: [dark bg or #0D1B2A];
  --color-surface: rgba(255,255,255,0.06);
  --color-text-primary: #FFFFFF;
  --color-text-muted: rgba(255,255,255,0.55);
  --color-border: rgba(255,255,255,0.10);
  --text-title: clamp(1.375rem, 2.8vw + 0.5rem, 2.25rem);
  --text-body: clamp(0.875rem, 1.4vw + 0.25rem, 1.125rem);
  --text-small: clamp(0.625rem, 0.8vw + 0.15rem, 0.75rem);
  --text-stat: clamp(2rem, 5vw + 0.5rem, 4rem);
}
.deck { height: 100vh; height: 100dvh; overflow: hidden; } /* dvh line always follows vh */
```
Never hardcode hex or px font sizes in elements — always the tokens above.

**No scrolling, ever.** Content that doesn't fit gets cut, not scrolled. Max per slide: 1 heading (argument), 5 bullets, 1 visual element, 1 footnote. Word-level caps (bullet length, slide body total, sentence length) live in `voice-and-brevity` — they are what make 5 bullets actually fit.

**Chrome (every slide):** thin header (company name, brand color, uppercase | project name, muted) + footer (your name | slide N/total | date). 9px max, metadata not content. Appendix slides show "APPENDIX A1" instead of project name.

**12 slide types:** Title/Cover, Executive Summary (3-card + stat callout), Section Divider, Insight/Analysis, Recommendation, Comparison/Tradeoffs (2-col), Metrics/KPI (card grid), Timeline/Roadmap, Process/Flowchart (Mermaid), Quote/Principle, Two-Column (current vs proposed), Appendix.

**Diagrams/charts — only CDN exceptions allowed:** Mermaid (`cdn.jsdelivr.net/npm/mermaid`) for flowcharts, Chart.js (`cdn.jsdelivr.net/npm/chart.js`) for bar/line/doughnut (no pie). Chart colors pull from `getComputedStyle(document.documentElement).getPropertyValue('--color-primary')`.

**Infographics (CSS-only, ≥1 per slide, max 2):** Stat Ring (conic-gradient donut) for a single %, Data Cluster for 3 hero numbers, Step Chain for process, Progress Bar for metric vs benchmark, 2×2 Matrix for priority, Before/After for current vs future. Must touch real slide data — never decorative.

**Navigation:** dot indicators only (no prev/next buttons), left/right arrow keys, touch swipe, `N` toggles speaker notes panel (hidden `<aside class="speaker-notes">`, shown on print/PDF too, under 100 words each).

**Print/PDF CSS — every slide must render, at the right page size:** since slides use `display: none` with a JS-toggled `.active` class, `@media print` must force every `.slide` back to visible or a PDF export captures only slide 1. It must also set an explicit `@page` size — without one, Chrome's print-to-pdf defaults to Letter portrait (8.5×11in) and squeezes a 16:9 deck into the wrong aspect ratio. Match the PPTX widescreen size (13.333in × 7.5in) so every export format shares one aspect ratio:
```css
@media print {
  @page { size: 13.333in 7.5in; margin: 0; }
  .navigation { display: none; }
  .deck { height: auto; overflow: visible; }
  .slide { display: flex !important; height: 7.5in; width: 13.333in; overflow: visible; page-break-after: always; }
}
```

**Speaker notes structure:** restate the heading differently → 2-3 sentences of narrative → transition line to next slide.

## Anti-patterns (never)
No accent lines under headings. No decorative card-edge color bars. No prev/next buttons. No CDN beyond Mermaid/Chart.js. No cream/beige backgrounds. No mixing dark/light slides. No more than 5 bullets. No hardcoded hex/px. No `100vh` without a following `100dvh`.

## QA before handoff
- [ ] Every `100vh` has `100dvh` on the next line
- [ ] No slide scrolls at 1280×800
- [ ] All sizes use `var(--text-*)` tokens
- [ ] Headings are arguments, not topics
- [ ] ≤5 bullets/slide, brand colors applied, dot count = slide count
- [ ] No sentence over 25 words, no bullet over 16, no core slide over 80 body words (`voice-and-brevity`)
- [ ] No placeholder text, file opens standalone with no console errors
- [ ] Print-to-PDF actually contains one page per slide, not just the active slide (check `@media print` overrides `display: none`)
