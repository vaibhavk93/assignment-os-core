# Presentation OS Architecture
## A Comprehensive Design Reference for the Assignment OS Multi-Agent Pipeline

**Version:** 1.0  
**Date:** 2026-07-05  
**Scope:** Formatter Agent (Agent 15), Visual QA Agent (Agent 16), and supporting skill layer  
**Supersedes:** Version 0 deck-builder.md and brand-templates.md (both skills remain active until v1 ships)

---

## Table of Contents

**Part I — Research Foundation**
1. Executive Summary
2. Research Methodology
3. Skill Ecosystem Survey
4. HTML Presentation Framework Comparison
5. PPTX Generation Library Comparison
6. Consulting Presentation Philosophy
7. AI Presentation Pipeline Survey
8. Data Visualization Principles
9. Accessibility Standards
10. PM Interview Presentation Standards

**Part II — Core Design Decisions**
11. Primary Format: HTML vs. PPTX
12. Dual-Track Architecture
13. Brand Color Persistence Strategy
14. Design Token System
15. Slide Type Taxonomy
16. Slide Layout Grid System
17. Typography System
18. Color System Architecture
19. Diagram vs. Bullet Decision Framework
20. Speaker Notes Handling

**Part III — HTML Track Architecture**
21. HTML Skill Structure
22. Viewport and Scaling Architecture
23. CSS Variable Hierarchy
24. Animation System
25. Navigation System
26. Responsive Breakpoints
27. CSS Anti-Patterns
28. Mermaid Diagram Integration
29. Chart.js Integration
30. PDF Export via Print CSS

**Part IV — PPTX Track Architecture**
31. PPTX Skill Structure
32. OOXML Hierarchy Model
33. Slide Master Strategy
34. python-pptx vs. PptxGenJS Decision
35. Placeholder vs. Shape Insertion
36. PPTX Slide Templates
37. Font Embedding Strategy
38. Image Handling
39. Color Fidelity in PPTX
40. Speaker Notes in PPTX

**Part V — Brand Intelligence Layer**
41. Brand Color Detection Protocol
42. Brandfetch API Integration
43. Fallback Color Hierarchy
44. Company_Memory Brand Caching
45. Color Contrast Validation

**Part VI — Quality Assurance Architecture**
46. Visual QA Agent Contract
47. HTML QA Checklist
48. PPTX QA Checklist
49. Accessibility QA Checklist
50. QA Failure Routing

**Part VII — Token Budget and Performance**
51. Token Budget Strategy
52. Agent Context Contracts
53. Multi-Format Parallelism
54. Caching Strategy
55. Error Recovery

**Part VIII — Skill File Specifications**
56. deck-builder.md v1 — Full Specification
57. pptx-builder.md v1 — Full Specification
58. brand-templates.md v1 — Updated Specification
59. presentation-checker.md — New Skill
60. Skill Frontmatter Requirements

**Part IX — Version 0 Gap Analysis**
61. deck-builder.md v0 Strengths
62. deck-builder.md v0 Weaknesses
63. brand-templates.md v0 Strengths
64. brand-templates.md v0 Weaknesses
65. Migration Path from v0 to v1

**Part X — Implementation Roadmap**
66. Phase 1: Foundation (Week 1)
67. Phase 2: HTML Track (Week 2)
68. Phase 3: PPTX Track (Week 3)
69. Phase 4: QA Integration (Week 4)
70. Final Recommendations

---

# Part I — Research Foundation

## 1. Executive Summary

Assignment OS produces interview deliverables. Every assignment ends in formatted output — most commonly an HTML slide deck or PPTX file. The current Version 0 skills (deck-builder.md and brand-templates.md) establish the pattern but contain critical gaps: no design token system, no brand persistence architecture, shallow QA checklist, CDN dependency in brand-templates.md (superseded but not fully resolved), limited slide type taxonomy, and no PPTX pathway.

This document architects Version 1 of the Presentation OS layer. It answers eight key design questions definitively, provides complete skill specifications, and establishes a quality gate that catches presentational failures before delivery.

**Eight key questions answered:**

| Question | Answer |
|---|---|
| HTML vs. PPTX as primary? | Dual-track. HTML primary for speed/fidelity; PPTX on request or when HITL selects it |
| Brand color persistence? | Company_Memory cache + Brandfetch API + 4-tier fallback hierarchy |
| Slide type taxonomy? | 12 canonical types, fully specified |
| QA pipeline design? | 22-point HTML checklist + 18-point PPTX checklist, binary pass/fail per item |
| CSS cross-browser approach? | CSS custom properties + clamp() + 100dvh fallback + no external dependencies |
| Diagrams vs. bullets? | Decision tree: relationship/process/comparison → diagram; list/evidence → bullets |
| Speaker notes handling? | HTML: excluded from visible render, accessible via print CSS; PPTX: native notes slides |
| Token budget? | Formatter reads draft.json only (~2k tokens); brand lookup cached in Company_Memory |

**Optimization target:** Interview hiring signal coverage — not visual novelty. Every design decision subordinates aesthetics to communication clarity, because hiring managers read fast and judge slow.

---

## 2. Research Methodology

Research covered 16 primary domains across two parallel search passes (8 queries each). Sources included official documentation, GitHub repositories with star counts, practitioner blogs from ex-MBB consultants, W3C/MDN specifications, npm package metadata, and AI platform product descriptions.

**Domains covered:**
- Anthropic SKILL.md structure and official PPTX skill
- Community skill marketplace (SkillsMP) best-in-class patterns
- PptxGenJS and python-pptx library architectures
- HTML presentation frameworks (reveal.js, Slidev, Marp, Bespoke.js)
- McKinsey/BCG/Bain consulting presentation philosophy
- Gamma.app and Beautiful.ai AI pipeline architectures
- Tufte data-ink ratio and Cole Nussbaumer Knaflic principles
- WCAG 2.1 AA accessibility standards
- PM interview presentation norms and evaluation criteria
- CSS clamp() and viewport unit architecture
- IBM Carbon and Material Design token systems
- Mermaid.js and Chart.js diagram integration patterns
- Brandfetch API brand color retrieval
- Consulting slide type taxonomy (15 canonical types from Deckary research)
- HTML-to-PPTX conversion quality (dom-to-pptx, html2ppt)
- Office Open XML / PPTX format specification (ISO/IEC 29500)

**Confidence level:** High on framework decisions; medium on PPTX conversion quality (evolving library landscape).

---

## 3. Skill Ecosystem Survey

### 3.1 Anthropic Official PPTX Skill

Located at `github.com/anthropics/skills`. The official skill handles reading, editing, and building PPTX files via python-pptx. Key pattern: YAML-driven content files per slide (`content.yaml`) with a global `style.yaml`. Slide content and styling are fully separated. Layout names in content YAML resolve against slide master layouts. This is the canonical pattern for python-pptx based generation.

### 3.2 Microsoft hve-core PowerPoint Skill

1,211 stars on SkillsMP. Uses python-pptx with YAML-driven content. Key insight: `--template` flag creates new presentation inheriting only slide masters, layouts, and theme from template PPTX — all existing slides discarded. `--source` flag for partial rebuilds preserves other slides. This two-mode approach is the right production pattern.

### 3.3 pptx-from-layouts Community Skill

Rated 95/100 on SkillsMP. Uses Slide Master layouts properly rather than inventory/replace approach. Includes three subagents: `pptx-outline-architect`, `pptx-template-onboarder`, `pptx-deck-qa`. Key principle: AI should select layouts by name from slide master, not construct shapes manually. This eliminates the most common python-pptx error (shape misalignment from manual coordinate calculation).

### 3.4 html-slides Community Skill (proyecto26)

Comprehensive HTML slide skill. Key specs:
- Every slide: `height: 100vh; height: 100dvh; overflow: hidden`
- All typography: `clamp(min, preferred, max)` — never fixed px
- Images: `max-height: min(50vh, 400px)`
- Responsive breakpoints at 700px, 600px, 500px viewport heights
- `prefers-reduced-motion` support mandatory
- CSS animations as baseline (no JS required for basic reveal)
- Mermaid CDN for technical diagrams

### 3.5 SKILL.md Frontmatter Structure

Required fields: `name`, `description`. Optional fields (up to 15): `model`, `allowed-tools`, `user-invokable`, `disable-model-invocation`, `context`, `hooks`, `subagent-types`, `version`, `author`, `tags`, `requires`, `extends`, `output`, `input`, `examples`. Skills stored at `~/.claude/skills/` or project-local at `.claude/skills/`.

---

## 4. HTML Presentation Framework Comparison

| Framework | Stars | Approach | Export | Best For |
|---|---|---|---|---|
| reveal.js | 71k | HTML/CSS/JS | PDF (print), hosted | Max control, branded decks |
| Slidev | 45k | Markdown + Vue | PDF, PPTX, PNG | Developer presentations |
| Marp | 30k+ | Markdown | PDF, PPTX, HTML | Speed, clean output |
| Bespoke.js | 4k | Micro-framework | None native | Custom minimal builds |
| Spectacle | 9k | React | None native | React-ecosystem teams |

**Decision for Assignment OS:** None of the above. Assignment OS generates self-contained single-file HTML without external dependencies (no CDN, no build tools). This is the pattern established by deck-builder.md v0 and confirmed correct by the html-slides community skill. Reveal.js CDN was explicitly superseded. The framework IS the generated HTML file itself — CSS custom properties + vanilla JS navigation.

**Rationale:** CDN dependency = failure mode in offline review. Build tool dependency = too much environment setup. Single-file HTML = email-safe, always works.

---

## 5. PPTX Generation Library Comparison

### 5.1 python-pptx

**Architecture:** OOXML abstraction in Python. Hierarchy: Theme → Slide Master → Slide Layout → Slide. Placeholders inherited and overridden at each level. Best pattern: open template PPTX, select layout by index, populate placeholders by idx (not position).

**Strengths:** Mature, well-documented, used by Anthropic official skill. Proper placeholder hierarchy support.

**Weaknesses:** Python dependency (Claude Code runs in Node/shell). Coordinate system in EMU (English Metric Units) is verbose. Manual shape placement requires precise math.

### 5.2 PptxGenJS

**Architecture:** JavaScript library. Fluent API: `new PptxGenJS()` → `addSlide()` → `addText()` / `addChart()` / `addShape()`. Supports `defineSlideMaster()`. Has `tableToSlides()` for converting HTML tables. OOXML-compliant output.

**Strengths:** JavaScript = no Python dependency. Runs in Node environment. Browser-safe. Better fit for Claude Code's execution environment.

**Weaknesses:** Lower-level than python-pptx for placeholder management. Less community tooling for layout-based approaches.

### 5.3 dom-to-pptx

**Architecture:** DOM traversal → computed style extraction → PptxGenJS shapes. Converts HTML elements to pixel-accurate PPTX. Handles CSS gradients, box-shadows, border-radius. Measures final x/y/width/height of every element (not CSS rules) — 100% visual accuracy regardless of layout method.

**Key limitation:** Does not read Flexbox/Grid definitions directly. Measures rendered output. This is actually the right approach for presentation conversion.

**Use case:** HTML-first workflow where PPTX is secondary export. Build HTML deck → dom-to-pptx → editable PPTX.

### 5.4 html2ppt (Java, spec-first)

Yoga-based flexbox layout engine. Compiles HTML+CSS to PPTX via Apache POI. Implements flexbox, spacing, sizing, absolute positioning, text, lists, tables, images, opacity, gradients, shadows, speaker notes. Most architecturally sound HTML→PPTX converter found. Limitation: Java dependency.

**Decision for Assignment OS PPTX track:**
- Primary: python-pptx (invoked via shell, Anthropic official pattern)
- Secondary: PptxGenJS when Python unavailable  
- HTML-to-PPTX bridge: dom-to-pptx for "export current HTML deck as PPTX"

---

## 6. Consulting Presentation Philosophy

Research across McKinsey, BCG, Bain sources (including ex-consultant blog Deckary, SlideScience, SlideWorks) yields consistent principles:

### 6.1 Pyramid Principle (Barbara Minto)

Answer first, then evidence. Structure: Situation → Complication → Question → Answer (SCQA). Executive reads title only and gets full argument. Body proves titles. Appendix holds detail.

### 6.2 Action Titles

Every slide title is a complete sentence stating the conclusion, not a topic label.
- Wrong: "Market Overview"
- Right: "Asian market growing 18% annually, 4x faster than Europe"

A reader flipping through titles alone should reconstruct the entire argument.

### 6.3 One Message Per Slide

One analytical unit per slide. If two insights exist, use two slides. McKinsey: one chart per slide. BCG: visual-first, chart-heavy. Bain: balanced.

### 6.4 MECE Structure

Arguments are Mutually Exclusive, Collectively Exhaustive. No overlap between slides, no gaps in coverage.

### 6.5 Ghost Deck Process

BCG: storylining session → sticky notes on wall → argument debates → complete action title sequence before opening PowerPoint. Output is ghost deck (skeleton with all titles). Only then does content slide construction begin. Assignment OS approximates this via Research Planner → Insight Synthesizer → Case Builder sequence.

### 6.6 Formatting Discipline (McKinsey Style)

- 2-3 colors maximum
- Sans-serif body (Arial/Helvetica/Inter), optional serif display
- Tight margins
- No drop shadows, no gradients (on shapes/backgrounds), no decorative elements
- Source line on every data chart (7-8pt)
- Consistent grid across entire deck
- Size hierarchy: Title 28-36pt, Subtitle 18-20pt, Body 11-12pt, Annotation 9-10pt, Footnote 7-8pt

### 6.7 BCG vs. McKinsey vs. Bain

| Element | BCG | McKinsey | Bain |
|---|---|---|---|
| Visual density | Chart-heavy, minimal text | Text-heavy, structured bullets | Balanced |
| Action titles | Punchy, quantitative | Comprehensive, logical | Clean, direct |
| Typical length | 30-40 slides | 50-80 slides | 30-50 slides |

**Assignment OS target:** BCG-adjacent. Short decks (8-15 slides), visual-first, quantitative action titles where data exists, data-light action titles where qualitative.

---

## 7. AI Presentation Pipeline Survey

### 7.1 Gamma.app Architecture

Pipeline: Prompt → Structure (outline) → Slide copy generation → Layout selection → Visual polish → Export. Uses 20+ models in parallel during generation. Output: branded slides with layouts. Exports to PDF/PPTX/hosted URL. Key insight: layout intelligence runs separately from copy generation.

### 7.2 Beautiful.ai Architecture

"Smart Slides" with deterministic layout intelligence. Each slide type has layout rules that adapt to content volume. More bullets → layout adapts, doesn't overflow. Key insight: slide layout is a function of content, not a fixed template.

### 7.3 Assignment OS Pipeline Position

Assignment OS is different from consumer AI presentation tools. It is not a "generate slides from prompt" system. It is a research-first, intent-driven system where slides express a pre-built argument. The Formatter agent receives `draft.json` — a fully structured recommendation with supporting evidence. Formatter's job is rendering, not generation.

This changes the design: Formatter needs high-fidelity rendering of structured content, not creative layout generation. The slide type for each piece of content is determined by content type, not by AI judgment at render time.

---

## 8. Data Visualization Principles

### 8.1 Tufte Principles

**Data-ink ratio:** Maximize data-ink (ink that carries information), minimize non-data ink (gridlines, borders, backgrounds, decorations). Every visual element that can be removed without information loss should be removed.

**Chartjunk:** Avoid 3D effects, excessive gridlines, decorative patterns, unnecessary legends. Chartjunk reduces data-ink ratio and increases cognitive load.

**Small multiples:** Same visual form repeated across conditions. Enables comparison. Better than animation or multiple chart types.

### 8.2 Cole Nussbaumer Knaflic Principles

1. Understand context (who, what, how)
2. Choose appropriate visual type
3. Eliminate clutter
4. Focus attention (pre-attentive attributes: color, size, position)
5. Tell a story
6. Practice makes perfect (iterate)

**Pre-attentive attributes for slides:** Color accent on key number/bar. Bold text for key phrase. Strategic whitespace to isolate key element.

### 8.3 Chart Type Decision Matrix

| Comparison Type | Chart Type |
|---|---|
| Part-to-whole | Pie (≤5 segments), Stacked bar |
| Ranking | Horizontal bar (sorted) |
| Trend over time | Line chart |
| Correlation | Scatter plot |
| Distribution | Histogram, box plot |
| Part of whole + trend | Stacked area |
| Single large number | KPI card with context |
| Relationship/flow | Mermaid flowchart |
| Process/sequence | Mermaid sequence or timeline |
| Hierarchy | Mermaid graph |

---

## 9. Accessibility Standards

### 9.1 WCAG 2.1 AA Requirements

**Color contrast — normal text (below 18pt regular or 14pt bold):** Minimum 4.5:1 ratio  
**Color contrast — large text (18pt+ regular or 14pt+ bold):** Minimum 3:1 ratio  
**Color contrast — UI components and graphical objects:** Minimum 3:1  
**AAA (aspirational):** 7:1 normal text, 4.5:1 large text

**Text resize:** Must scale to 200% without loss of content or functionality. CSS `clamp()` must have maximum ≥ 2× minimum.

**Reduced motion:** `prefers-reduced-motion: reduce` media query must disable or reduce animations.

**Focus indicators:** Keyboard navigable elements need visible focus ring.

### 9.2 Presentation-Specific Accessibility

Speaker notes serve as audio description equivalent for blind attendees using NVDA/JAWS. Alt text on all meaningful images. Color never sole carrier of meaning (also use shape, pattern, label). Slide structure via semantic HTML (`<section>`, `<h1>`, `<p>`).

### 9.3 Contrast Checking Protocol

Before finalizing any brand color combination:
1. Extract brand primary, background, and text colors
2. Calculate contrast ratio: `(L1 + 0.05) / (L2 + 0.05)` where L = relative luminance
3. If text-on-background < 4.5:1, lighten background or darken text
4. If branded accent on white < 4.5:1, use accent for decorative elements only, not body text

---

## 10. PM Interview Presentation Standards

### 10.1 Context

PM interview presentations increased significantly post-2020. Common formats: take-home case (24-48 hours), live case (60-90 minutes), design exercise (present wireframe/strategy). BCG written case: 3-5 slides from scratch in 1.5-2 hours. Increasing prevalence of structured deliverables.

### 10.2 Evaluation Criteria

Hiring managers assess:
1. Structure quality (pyramid principle applied? MECE?)
2. Insight quality (did they find the non-obvious insight?)
3. Effort signal (polished vs. rushed)
4. Data usage (quantified claims vs. vague assertions)
5. Recommendation clarity (what exactly do you recommend and why?)
6. Assumption awareness (what did they have to assume and do they know it?)

**Key finding:** Structure quality > creativity. A well-structured slide with a clear action title beats a "creative" slide with unclear message every time. Effort shows and matters. A deck that looks like 8 hours of work signals investment even if the hiring signal content is identical.

### 10.3 Format Preference

Most PM roles: Google Slides or PowerPoint preferred for editable format. HTML slides increasingly accepted, especially at tech companies. Key constraint: slides must be shareable (email-safe). HTML single-file satisfies this. Multi-file HTML does not.

---

# Part II — Core Design Decisions

## 11. Primary Format: HTML vs. PPTX

**Decision: Dual-track, HTML primary.**

HTML is generated by default for every assignment. PPTX is generated when:
1. User selects PPTX at `/output-select` HITL gate
2. Assignment type classifier flags `pptx_preferred: true` (e.g., BCG written case)
3. Company_Memory indicates hiring manager prefers PPTX

**Rationale for HTML primary:**
- Self-contained single file, email-safe
- No font rendering differences across OS
- Full CSS control — brand fidelity higher than PPTX
- Mermaid/Chart.js diagrams render natively
- No PowerPoint license required for viewing
- CDN-free (all inline) = offline-safe

**Rationale for PPTX secondary:**
- Editable after delivery (hiring manager preference documented)
- Familiar format, no "how do I run this" friction
- Required for some company formats
- Enables slide-by-slide commenting

**When both formats generated:** Formatter spawns two parallel subagents (one HTML, one PPTX). Visual QA runs on both. State updated with both outputs.

---

## 12. Dual-Track Architecture

```
draft.json
    │
    ├─── Formatter (HTML) ──→ OUTPUTS/deck.html ──→ Visual QA (HTML)
    │
    └─── Formatter (PPTX) ──→ OUTPUTS/deck.pptx ──→ Visual QA (PPTX)
```

Both tracks read from the same `draft.json`. Neither track has knowledge of the other's output. QA failures route back to the respective Formatter instance — not to Case Builder (which would trigger a Checker loop).

**Token budget implication:** Each Formatter instance reads only `draft.json` (approximately 2,000-4,000 tokens). Brand lookup is pre-cached in Company_Memory. Total Formatter context: ~6,000 tokens including skill file.

---

## 13. Brand Color Persistence Strategy

**The problem:** Every assignment for the same company should use the same brand colors. Currently this requires re-detecting brand colors each run, wasting tokens and potentially producing inconsistent results.

**Solution: Four-tier hierarchy**

**Tier 1 — Company_Memory cache (fastest)**  
Check `Companies/<Company>/Company_Memory.md` for existing brand color block. If found and `brand_confidence == "confirmed"`, use directly. No API call.

**Tier 2 — Brandfetch API lookup**  
If Company_Memory has no brand block or confidence is "low", query Brandfetch API: `GET https://api.brandfetch.io/v2/brands/<domain>`. Returns `colors[]` array with `hex` and `type` fields. Cache result back to Company_Memory with `brand_confidence: "confirmed"`.

**Tier 3 — Web scraping**  
If Brandfetch returns no results (rare — covers 50M+ brands), use WebFetch on company homepage. Extract dominant colors from CSS variables, meta theme-color, logo SVG fill attributes. Cache with `brand_confidence: "scraped"`.

**Tier 4 — Assignment OS defaults**  
If all lookup fails, use assignment OS professional palette. Do NOT use the old navy/blue defaults from brand-templates.md v0 (those signal generic, not company-specific). Use: `#1B2A4A` (deep navy), `#E8E8E8` (light gray), `#2C7BE5` (professional blue). Flag in state.json that brand colors are defaults — prompt HITL awareness.

**Brand block format in Company_Memory.md:**
```
## Brand Colors
brand_primary: "#EC5B24"
brand_secondary: "#1B1B1B"
brand_tertiary: "#FAC8A5"
brand_background: "#FFFFFF"
brand_text: "#1B1B1B"
brand_confidence: "confirmed"
brand_source: "brandfetch"
brand_retrieved: "2026-07-05"
```

---

## 14. Design Token System

Design tokens are named CSS custom properties that carry all theming decisions. No hardcoded colors, font sizes, or spacing values anywhere in generated HTML.

**Token categories:**

```css
:root {
  /* Brand Colors */
  --color-primary: #EC5B24;
  --color-secondary: #1B1B1B;
  --color-accent: #FAC8A5;
  --color-background: #FFFFFF;
  --color-surface: #F8F8F8;
  --color-text-primary: #1B1B1B;
  --color-text-secondary: #666666;
  --color-text-muted: #999999;
  --color-border: #E0E0E0;

  /* Typography */
  --font-heading: 'Inter', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Type Scale (fluid via clamp) */
  --text-hero: clamp(2.5rem, 5vw + 1rem, 4.5rem);
  --text-title: clamp(1.8rem, 3.5vw + 0.5rem, 3rem);
  --text-heading: clamp(1.3rem, 2vw + 0.3rem, 2rem);
  --text-subhead: clamp(1rem, 1.5vw + 0.2rem, 1.5rem);
  --text-body: clamp(0.875rem, 1vw + 0.1rem, 1.125rem);
  --text-small: clamp(0.75rem, 0.8vw, 0.875rem);
  --text-caption: clamp(0.65rem, 0.7vw, 0.75rem);

  /* Spacing (8px base unit, IBM Carbon pattern) */
  --space-1: 0.5rem;   /* 8px */
  --space-2: 1rem;     /* 16px */
  --space-3: 1.5rem;   /* 24px */
  --space-4: 2rem;     /* 32px */
  --space-6: 3rem;     /* 48px */
  --space-8: 4rem;     /* 64px */
  --space-10: 5rem;    /* 80px */

  /* Border */
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-lg: 16px;
  --border-width: 1px;

  /* Motion */
  --duration-fast: 150ms;
  --duration-normal: 300ms;
  --duration-slow: 600ms;
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
}
```

**Constraint:** All 7 slide types use only tokens — never hardcoded values. Brand customization requires changing only `:root` block. Deck remains internally consistent regardless of brand.

---

## 15. Slide Type Taxonomy

Assignment OS supports 12 canonical slide types. Each type maps to a specific HTML template and PPTX layout name.

| # | Type | Purpose | Layout Pattern |
|---|---|---|---|
| 1 | **Title / Cover** | Opening slide | Full-viewport hero, company name, role, candidate name |
| 2 | **Executive Summary** | 3-column insight cards | Three balanced columns, each with headline + 2-3 bullets |
| 3 | **Section Divider** | Structural break | Full-bleed accent color, section number + title |
| 4 | **Insight / Analysis** | Single finding with evidence | Action title + one dominant visual (chart or callouts) |
| 5 | **Recommendation** | Decision or direction | Large action statement + 3 supporting reasons |
| 6 | **Comparison / Tradeoffs** | Side-by-side options | 2-3 column comparison with header labels |
| 7 | **Metrics / KPI** | Data dashboard | Card grid (2×2 or 3×2) with metric value, label, trend |
| 8 | **Timeline / Roadmap** | Phases or sequence | Horizontal timeline with milestones or vertical phases |
| 9 | **Process / Flowchart** | System or workflow | Mermaid diagram or structured flow boxes |
| 10 | **Quote / Principle** | Emphasis moment | Centered large quote with attribution |
| 11 | **Two-Column** | Text + visual split | 50/50 or 60/40 split layout |
| 12 | **Appendix** | Supporting detail | Dense content, smaller typography, source-heavy |

**Classification rule in draft.json:**

```json
{
  "slides": [
    {
      "slide_type": "executive_summary",
      "action_title": "Three growth vectors each worth $50M+ represent untapped white space",
      "content": { ... }
    }
  ]
}
```

Formatter selects HTML template and PPTX layout based on `slide_type` field. Case Builder is responsible for assigning correct type during draft construction.

---

## 16. Slide Layout Grid System

Based on IBM Carbon 2x Grid principle: 8px base unit, multiples of 8 for all spacing.

**Slide canvas:** 1280×720px (16:9, standard presentation aspect ratio)  
**Content area:** 1152×608px (64px margin all sides = 8 × 8px units)  
**Column grid:** 12 columns, 24px gutter, auto-width columns  
**Safe zone for titles:** Top 120px (for action title, consistent position across all slides)  
**Safe zone for footer:** Bottom 48px (slide number, source, logo if needed)  

**HTML implementation:**
```css
.slide {
  height: 100vh;
  height: 100dvh;
  overflow: hidden;
  display: grid;
  grid-template-rows: 120px 1fr 48px;
  padding: var(--space-4) var(--space-8);
  box-sizing: border-box;
}
.slide-title { grid-row: 1; }
.slide-content { grid-row: 2; overflow: hidden; }
.slide-footer { grid-row: 3; }
```

**Content overflow rule:** If content exceeds capacity, split across two slides. Never scroll within a slide. Never shrink font below `--text-body` minimum.

---

## 17. Typography System

**Font loading strategy:** System fonts for body, Google Fonts `crossorigin="anonymous"` for headings (enables dom-to-pptx font embedding). Fallback to system stack.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" 
      rel="stylesheet" crossorigin="anonymous">
```

**Font embedding in PPTX:** dom-to-pptx auto-embeds fonts when `autoEmbedFonts: true` and CORS headers present. Inter from Google Fonts with `crossorigin` attribute satisfies this.

**Type hierarchy:**
- Hero (Title slide): `--text-hero`, weight 700
- Action title (all slides): `--text-title`, weight 600, color `--color-text-primary`
- Section heading: `--text-heading`, weight 600
- Subheading / card title: `--text-subhead`, weight 600
- Body text: `--text-body`, weight 400
- Bullet text: `--text-body`, weight 400, `--color-text-secondary`
- Caption / source: `--text-caption`, weight 400, `--color-text-muted`

**clamp() compliance rule:** Every clamp must satisfy: maximum ≥ 2× minimum (WCAG 1.4.4 resize text at 200%). Example: `clamp(1rem, 2.5vw, 2rem)` passes. `clamp(1rem, 2.5vw, 1.4rem)` fails.

---

## 18. Color System Architecture

**Primary palette:** 5 brand colors loaded from Company_Memory (via tokens)  
**Semantic palette:** Success (#16A34A), Warning (#D97706), Error (#DC2626), Info (#2563EB)  
**Neutral palette:** 9-step gray scale from #F9FAFB to #111827

**Color usage rules:**
1. Accent color (`--color-primary`) for: slide number, key metric highlight, section header background, callout box border, chart primary bar
2. Never use accent for body text (may fail contrast)
3. Text always `--color-text-primary` or `--color-text-secondary` — never raw brand color
4. Background always white or `--color-surface` (near-white) — never dark unless Title/Section Divider slide
5. Mixed dark/light slides prohibited (consistency breaks visual flow)

**Contrast validation at render time:**
- Text-on-background: must ≥ 4.5:1
- Accent-on-white: calculate; if < 4.5:1, use `--color-text-primary` for text, accent for decorative only
- If brand primary fails contrast on white, create a darker variant: `--color-primary-dark` at 70% lightness

---

## 19. Diagram vs. Bullet Decision Framework

Decision tree for Case Builder when assigning content to slide types:

```
Content has discrete items with no relationship?
  → Bullet list (max 5 bullets, max 8 words each)

Content shows relationship between parts?
  → Flowchart (Mermaid graph/flowchart)

Content shows sequence or process?
  → Process slide (Mermaid sequence or custom flow)

Content shows change over time?
  → Timeline slide OR line chart

Content compares two or more options?
  → Comparison slide (table or side-by-side)

Content is a single large number with context?
  → KPI card (Metrics slide type)

Content has multiple data points across categories?
  → Chart slide (Chart.js bar/line/pie)

Content is a recommendation with supporting logic?
  → Recommendation slide (statement + reasons)
```

**Anti-pattern:** Converting inherently visual information into bullets. A 5-step process described in 5 bullets is always inferior to a 5-step flow diagram. If the relationship matters, diagram it.

**Maximum bullets per slide:** 5. Maximum words per bullet: 8 (action title excluded). If content requires more, split slide or move to Appendix.

---

## 20. Speaker Notes Handling

**HTML track:** Speaker notes are excluded from the visible slide render. They exist in the HTML DOM as `<aside class="speaker-notes">` inside each `<section>`. Hidden via CSS (`display: none`). Accessible via print CSS for PDF export of notes view. Keyboard shortcut 'N' toggles notes panel for presenter.

```html
<section class="slide">
  <div class="slide-content"><!-- visible content --></div>
  <aside class="speaker-notes">
    These notes visible only in presenter mode or PDF notes export.
    Include: talking points, source citations, data caveats, anticipated Q&A.
  </aside>
</section>
```

**PPTX track:** Native PowerPoint notes slides via python-pptx `notes_slide.notes_text_frame`. Speaker notes do not appear in normal slide view, only in presenter view.

**Content of speaker notes (populated by Case Builder in draft.json):**
- 3-5 key talking points for that slide
- Source citations for any data claims
- Anticipated objections and responses
- Transition to next slide

**Notes never appear in hiring manager view** unless they explicitly enter presenter mode. This is intentional — notes are for live presentation prep, not for read-review submission.

---

# Part III — HTML Track Architecture

## 21. HTML Skill Structure

`deck-builder.md` v1 skill structure:

```yaml
---
name: deck-builder
description: Generates self-contained single-file HTML presentation decks for Assignment OS. Triggered when Formatter receives draft.json and output format includes "html". Reads draft.json only. Produces OUTPUTS/CompanyName_AssignmentType_YYYY-MM-DD.html.
version: 1.0
model: claude-sonnet-4-5
allowed-tools: Read, Write, WebFetch
user-invokable: false
---
```

**Execution flow:**
1. Read `draft.json` from workspace/
2. Read brand colors from Company_Memory.md brand block
3. Validate: check_report.json.verdict == "PASS" (hard gate)
4. Determine slide count and type sequence
5. Select HTML template for each slide type
6. Inject design tokens with brand colors
7. Generate complete HTML with inline CSS and JS
8. Write to OUTPUTS/ with correct filename
9. Return manifest (slide count, types used, file size)

---

## 22. Viewport and Scaling Architecture

Every slide must be viewport-fitted. Full specification:

```css
/* Base slide rules — mandatory for every presentation */
.presentation {
  width: 100%;
  height: 100vh;
  height: 100dvh; /* iOS Safari fix — overrides 100vh if supported */
  overflow: hidden;
  position: relative;
}

.slide {
  width: 100%;
  height: 100vh;
  height: 100dvh;
  overflow: hidden;
  display: none; /* hidden by default, JS shows active */
  box-sizing: border-box;
  position: absolute;
  top: 0;
  left: 0;
}

.slide.active {
  display: grid;
}

/* iOS 100vh bug: always pair 100vh with 100dvh */
/* 100dvh = dynamic viewport height = excludes browser chrome */
/* 100svh = small viewport height = includes browser chrome */
/* Use 100dvh for best mobile compatibility */
```

**Responsive height breakpoints (from html-slides community skill):**
```css
@media (max-height: 700px) {
  /* Reduce padding, tighten spacing */
  .slide { padding: var(--space-2) var(--space-4); }
}

@media (max-height: 600px) {
  /* Reduce font sizes, compress layout */
  :root { --text-body: clamp(0.75rem, 0.9vw, 0.95rem); }
}

@media (max-height: 500px) {
  /* Landscape mobile — hide non-essential elements */
  .slide-footer { display: none; }
}
```

**Image height constraint:**
```css
img {
  max-height: min(50vh, 400px);
  width: auto;
  object-fit: contain;
}
```

---

## 23. CSS Variable Hierarchy

CSS variables cascade normally — slide-level overrides root when needed.

```css
/* Root: global tokens */
:root { --color-bg: #FFFFFF; }

/* Slide type override: dark slides */
.slide[data-type="title"],
.slide[data-type="section-divider"] {
  --color-bg: var(--color-secondary);
  --color-text-primary: #FFFFFF;
  --color-text-secondary: rgba(255,255,255,0.75);
}

/* Component override: callout box */
.callout {
  --color-bg: var(--color-surface);
  border-left: 3px solid var(--color-primary);
  background: var(--color-bg);
}
```

This hierarchy prevents hardcoded exceptions. Dark slide reversal happens via data attribute, not class override spaghetti.

---

## 24. Animation System

**CSS-first approach (default):**
```css
/* Elements start hidden */
.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity var(--duration-normal) var(--ease-out),
              transform var(--duration-normal) var(--ease-out);
}

/* Staggered reveal on slide activation */
.slide.active .reveal {
  opacity: 1;
  transform: translateY(0);
}

.slide.active .reveal:nth-child(1) { transition-delay: 0ms; }
.slide.active .reveal:nth-child(2) { transition-delay: 100ms; }
.slide.active .reveal:nth-child(3) { transition-delay: 200ms; }
.slide.active .reveal:nth-child(4) { transition-delay: 300ms; }
.slide.active .reveal:nth-child(5) { transition-delay: 400ms; }

/* Reduced motion: no animation */
@media (prefers-reduced-motion: reduce) {
  .reveal {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

**No GSAP, no external animation library.** CSS animations are sufficient and eliminate external dependency.

---

## 25. Navigation System

```javascript
// Self-contained navigation — no external dependencies
(function() {
  const slides = document.querySelectorAll('.slide');
  let current = 0;

  function show(n) {
    slides.forEach(s => s.classList.remove('active'));
    current = Math.max(0, Math.min(n, slides.length - 1));
    slides[current].classList.add('active');
    updateIndicator();
  }

  function updateIndicator() {
    document.querySelectorAll('.dot').forEach((d, i) => {
      d.classList.toggle('active', i === current);
    });
    document.querySelector('.slide-counter').textContent = 
      `${current + 1} / ${slides.length}`;
  }

  // Keyboard navigation
  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
      e.preventDefault();
      show(current + 1);
    }
    if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
      e.preventDefault();
      show(current - 1);
    }
    if (e.key === 'n' || e.key === 'N') {
      document.querySelector('.speaker-notes-panel')?.classList.toggle('visible');
    }
  });

  // Touch/swipe support
  let touchStartX = 0;
  document.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; });
  document.addEventListener('touchend', e => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) show(diff > 0 ? current + 1 : current - 1);
  });

  show(0);
})();
```

**Navigation controls:** Dot indicators (not prev/next buttons — confirmed v0 anti-pattern). Slide counter (`3 / 12`) in bottom-right corner. Keyboard arrows and spacebar. Touch swipe.

---

## 26. Responsive Breakpoints

Presentations viewed on various screens. Primary target: 1280×720 laptop display. Secondary: 1920×1080 external monitor. Tertiary: 375×812 mobile (review only, not presentation mode).

Breakpoint strategy: **height-driven** (not width-driven). Slides are height-constrained by nature.

| Viewport height | Adjustment |
|---|---|
| > 768px | Full layout, normal spacing |
| 600-768px | Compressed padding, slightly smaller type |
| 480-600px | Minimum type sizes, compressed cards |
| < 480px | Emergency layout: single column, hide decorative elements |

No layout changes at width breakpoints — slides are fixed 16:9 aspect. Width breakpoints only affect text reflow within columns.

---

## 27. CSS Anti-Patterns

These are explicitly prohibited in generated HTML:

| Anti-pattern | Reason |
|---|---|
| Scrolling within a slide | Violates viewport-fitted architecture |
| Fixed pixel font sizes | Breaks accessibility zoom, violates clamp requirement |
| `overflow: auto` on slide | Allows hidden content — content must be split |
| Inline style attributes | Prevents brand customization, creates specificity conflicts |
| CDN references | Creates external dependency, offline failure mode |
| Dark + light slide mixing | Breaks visual rhythm, confuses brand system |
| Accent lines under headings | Generic, not brand-aligned |
| Decorative color bars | Chartjunk, reduces data-ink ratio |
| Prev/Next buttons | Poor visual design; use dots + keyboard |
| Cream/beige backgrounds | Signals low quality; use white or `--color-surface` |
| > 5 bullets per slide | Cognitive overload; split slide |
| > 8 words per bullet | Sentence creep; compress to phrase |
| Mixed font families | Use heading/body token only |
| Hardcoded hex values | Must use CSS variable tokens |
| Purple gradients | Generic "AI slop" aesthetic |
| `Inter` everywhere | Use brand font stack from tokens |

---

## 28. Mermaid Diagram Integration

Mermaid supported via CDN (exception to no-CDN rule — diagram content only, not layout/style).

```html
<!-- Place in <head> -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.9.0/mermaid.min.js"></script>
<script>
  mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    themeVariables: {
      primaryColor: 'var(--color-primary)',
      primaryTextColor: 'var(--color-text-primary)',
      primaryBorderColor: 'var(--color-border)',
      lineColor: 'var(--color-text-secondary)',
      background: 'var(--color-background)',
      fontSize: '14px'
    }
  });
</script>

<!-- Usage in slide -->
<pre class="mermaid">
flowchart LR
  A[User] --> B{Auth Check}
  B -->|Pass| C[Dashboard]
  B -->|Fail| D[Login]
</pre>
```

**Supported diagram types:** Flowchart, Sequence, State, Gantt, User Journey, Class, ER, Pie. Use flowchart for process maps, sequence for system interactions, gantt for roadmaps.

**When to use Mermaid vs. CSS layout:** Use Mermaid when the relationship structure is complex (more than 4-5 connected nodes or steps). Use CSS layout (flex boxes with arrows) for simple 3-4 step linear processes.

---

## 29. Chart.js Integration

Chart.js for data visualizations. Inline CDN (exception alongside Mermaid).

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>

<!-- Usage -->
<canvas id="chart-revenue" width="600" height="350"></canvas>
<script>
new Chart(document.getElementById('chart-revenue'), {
  type: 'bar',
  data: {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    datasets: [{
      data: [120, 145, 189, 210],
      backgroundColor: 'var(--color-primary)',
      borderRadius: 4
    }]
  },
  options: {
    plugins: {
      legend: { display: false }
    },
    scales: {
      y: { grid: { color: 'var(--color-border)' } },
      x: { grid: { display: false } }
    }
  }
});
</script>
```

**Chart selection rules:** Apply section 8.3 chart type matrix. Never 3D. Never pie with > 5 segments (use grouped bar). Label data points directly on charts when ≤ 6 data points (eliminates legend). Source citation required below every chart.

---

## 30. PDF Export via Print CSS

```css
@media print {
  /* One slide per page */
  .slide {
    page-break-after: always;
    height: 100vh;
    overflow: visible; /* Allow content to be visible in print */
    display: block !important;
    position: static;
    opacity: 1 !important;
    transform: none !important;
  }

  /* Show all slides, not just active */
  .slide { display: block; }

  /* Hide navigation elements */
  .slide-counter,
  .dot-indicators,
  .speaker-notes-panel { display: none; }

  /* Reveal all hidden content */
  .reveal {
    opacity: 1 !important;
    transform: none !important;
  }

  /* Notes view: show speaker notes */
  @page { size: A4 landscape; margin: 0; }
}
```

Print CSS enables: browser File → Print → Save as PDF for a clean PDF export with one slide per page. Speaker notes visible in separate print pass with notes CSS class active.

---

# Part IV — PPTX Track Architecture

## 31. PPTX Skill Structure

`pptx-builder.md` v1 skill structure:

```yaml
---
name: pptx-builder
description: Generates PPTX presentation files for Assignment OS using python-pptx (primary) or PptxGenJS (fallback). Only runs after check_report.json.verdict == "PASS". Reads draft.json only. Produces OUTPUTS/CompanyName_AssignmentType_YYYY-MM-DD.pptx.
version: 1.0
model: claude-sonnet-4-5
allowed-tools: Read, Write, Bash
user-invokable: false
---
```

---

## 32. OOXML Hierarchy Model

PPTX format (ISO/IEC 29500) ZIP+XML archive:

```
presentation.pptx (ZIP)
├── ppt/
│   ├── presentation.xml          ← slide references, deck metadata
│   ├── theme/theme1.xml           ← colors, fonts, effects
│   ├── slideMasters/
│   │   └── slideMaster1.xml      ← master layout, default styles
│   ├── slideLayouts/
│   │   ├── slideLayout1.xml      ← Title slide layout
│   │   ├── slideLayout2.xml      ← Content layout
│   │   └── ...                   ← one per layout type
│   ├── slides/
│   │   ├── slide1.xml            ← individual slide content
│   │   └── ...
│   ├── notesSlides/
│   │   └── notesSlide1.xml       ← speaker notes per slide
│   └── media/                    ← images, embedded files
```

**Hierarchy of inheritance:** Theme → Slide Master → Slide Layout → Slide  
Properties defined at higher level are inherited below. Slides override layouts, layouts override master.

---

## 33. Slide Master Strategy

**Approach:** Use a pre-built template PPTX with slide masters already configured for the 12 slide types. Formatter loads this template and populates placeholders.

**Template PPTX location:** `Global/templates/assignment-os-base.pptx`

Template contains:
- Slide Master 1: Standard light theme (white background)
- 12 Slide Layouts, named to match taxonomy: "Title", "Exec Summary", "Section Divider", "Insight Analysis", "Recommendation", "Comparison", "Metrics KPI", "Timeline Roadmap", "Process Flowchart", "Quote Principle", "Two Column", "Appendix"

**python-pptx pattern:**
```python
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor

# Load template
prs = Presentation('Global/templates/assignment-os-base.pptx')

# Add slide from named layout
layout_name = "Insight Analysis"
layout = next(l for l in prs.slide_master.slide_layouts if l.name == layout_name)
slide = prs.slides.add_slide(layout)

# Populate placeholders by idx
for ph in slide.placeholders:
    if ph.placeholder_format.idx == 0:  # Title
        ph.text = slide_data['action_title']
    elif ph.placeholder_format.idx == 1:  # Body
        ph.text = slide_data['body_text']

# Apply brand color to title
title_ph = slide.placeholders[0]
title_ph.text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(0x1B, 0x1B, 0x1B)
```

---

## 34. python-pptx vs. PptxGenJS Decision

**Primary: python-pptx**  
Reasoning: Anthropic official PPTX skill uses it. Most complete OOXML abstraction. Proper placeholder hierarchy support. Required for template-based approach.

**Execution:** Claude Code invokes via Bash: `python3 pptx_builder.py --draft workspace/draft.json --output OUTPUTS/deck.pptx --brand Company_Memory.md`

**Fallback: PptxGenJS**  
When: Python unavailable in execution environment, or when Formatter is building PPTX from scratch without template.

```javascript
const PptxGenJS = require('pptxgenjs');
const pptx = new PptxGenJS();

pptx.defineSlideMaster({
  title: 'ASSIGNMENT_OS_MASTER',
  background: { color: 'FFFFFF' },
  objects: [
    { line: { x: 0, y: 6.5, w: '100%', h: 0, line: { color: 'E0E0E0', pt: 1 } } }
  ]
});

const slide = pptx.addSlide({ masterName: 'ASSIGNMENT_OS_MASTER' });
slide.addText(action_title, { x: 0.5, y: 0.3, w: '90%', h: 1.2, fontSize: 28, bold: true, color: '1B1B1B' });
```

---

## 35. Placeholder vs. Shape Insertion

**Rule:** Always prefer placeholder population over manual shape insertion.

**Why:** Placeholders inherit Master/Layout formatting. Manual shapes bypass inheritance, requiring explicit styling for every attribute. This produces bloated code and inconsistent results.

**When to use manual shapes:** Charts (no placeholder type for charts in OOXML), images at specific positions, decorative elements.

**Placeholder idx reference:**
| idx | Placeholder Type |
|---|---|
| 0 | Title |
| 1 | Body / Content |
| 2 | Date |
| 3 | Slide number |
| 4 | Footer |
| 10+ | Custom content areas |

---

## 36. PPTX Slide Templates

Each of the 12 slide types maps to a python-pptx construction pattern. Sample for Recommendation:

```python
def build_recommendation_slide(prs, data, brand):
    layout = get_layout(prs, "Recommendation")
    slide = prs.slides.add_slide(layout)
    
    # Action title
    slide.placeholders[0].text = data['action_title']
    
    # Main recommendation statement (large, centered)
    txBox = slide.shapes.add_textbox(Inches(1), Inches(1.8), Inches(8), Inches(1.5))
    tf = txBox.text_frame
    tf.text = data['recommendation_statement']
    tf.paragraphs[0].font.size = Pt(24)
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.color.rgb = RGBColor(*hex_to_rgb(brand['primary']))
    
    # Three supporting reasons
    for i, reason in enumerate(data['reasons'][:3]):
        y_pos = Inches(3.5 + i * 0.9)
        box = slide.shapes.add_textbox(Inches(1), y_pos, Inches(8), Inches(0.7))
        tf = box.text_frame
        run = tf.paragraphs[0].add_run()
        run.text = f"• {reason}"
        run.font.size = Pt(16)
    
    # Speaker notes
    notes_slide = slide.notes_slide
    notes_slide.notes_text_frame.text = '\n'.join(data.get('speaker_notes', []))
    
    return slide
```

---

## 37. Font Embedding Strategy

**python-pptx:** Fonts used in PPTX must be available on viewer's machine OR embedded. python-pptx does not natively embed fonts. Workaround: use only safe cross-platform fonts (Calibri, Arial, Helvetica) in PPTX track, or specify fonts available on both Windows (Calibri) and macOS (Calibri via Office).

**Recommended font stack for PPTX:**
- Heading: Calibri Bold (bundled with all Office installations)
- Body: Calibri (bundled with all Office installations)
- Fallback: Arial

**Note:** This differs from HTML track (Inter). Acceptable — PPTX is the editable format, HTML is the presentation format. Font choice optimizes for each medium.

---

## 38. Image Handling

**HTML track:** Images encoded as base64 inline data URIs for self-contained file.
```html
<img src="data:image/png;base64,[base64_data]" alt="Revenue growth chart">
```

**PPTX track:** Images added via python-pptx `add_picture()`:
```python
from pptx.util import Inches
slide.shapes.add_picture('chart_export.png', Inches(1), Inches(2), Inches(8), Inches(4))
```

**Chart export pipeline:** For Chart.js charts in HTML, export to PNG via puppeteer (headless Chrome). Save to temp file. Include in PPTX via `add_picture()`. This enables identical chart visualization across both tracks.

---

## 39. Color Fidelity in PPTX

PPTX colors specified as RGB hex in OOXML. python-pptx uses `RGBColor(r, g, b)` with integer values 0-255.

```python
def hex_to_rgb(hex_color):
    """Convert #EC5B24 to (236, 91, 36)"""
    h = hex_color.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# Usage
color = RGBColor(*hex_to_rgb(brand['primary']))
```

**Theme colors:** OOXML theme defines 12 semantic colors (dk1, lt1, dk2, lt2, accent1-6, hlink, folHlink). Using theme color references instead of explicit RGB enables PowerPoint's native color scheme switching. Assign brand primary to `accent1` in theme for maximum compatibility.

---

## 40. Speaker Notes in PPTX

```python
# Add speaker notes to any slide
notes_slide = slide.notes_slide
tf = notes_slide.notes_text_frame
tf.clear()

p = tf.paragraphs[0]
p.text = slide_data.get('speaker_notes_intro', '')

for note in slide_data.get('speaker_notes', []):
    p = tf.add_paragraph()
    p.text = f"• {note}"
```

Notes viewable in PowerPoint presenter view. Not visible in normal slide view. Exports to PDF with speaker notes option in PowerPoint.

---

# Part V — Brand Intelligence Layer

## 41. Brand Color Detection Protocol

**Step 1: Check Company_Memory**
```python
def get_brand_colors(company_name):
    memory_path = f"Companies/{company_name}/Company_Memory.md"
    memory = read_file(memory_path)
    brand_block = parse_brand_block(memory)
    
    if brand_block and brand_block.get('brand_confidence') == 'confirmed':
        return brand_block  # Cache hit
    
    # Cache miss — proceed to Brandfetch
    return fetch_brand_colors_brandfetch(company_name)
```

**Step 2: Brandfetch API**
```python
import requests

def fetch_brand_colors_brandfetch(domain):
    url = f"https://api.brandfetch.io/v2/brands/{domain}"
    headers = {"Authorization": f"Bearer {BRANDFETCH_API_KEY}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return fallback_colors()
    
    data = response.json()
    colors = data.get('colors', [])
    
    primary = next((c['hex'] for c in colors if c.get('type') == 'primary'), None)
    secondary = next((c['hex'] for c in colors if c.get('type') == 'secondary'), None)
    
    if not primary:
        return fallback_colors()
    
    result = {
        'brand_primary': primary,
        'brand_secondary': secondary or '#1B1B1B',
        'brand_confidence': 'confirmed',
        'brand_source': 'brandfetch'
    }
    
    # Cache to Company_Memory
    update_company_memory_brand_block(result)
    return result
```

---

## 42. Brandfetch API Integration

**Endpoint:** `GET https://api.brandfetch.io/v2/brands/{domain}`  
**Auth:** Bearer token in Authorization header  
**Free tier:** 100 requests/month (sufficient for assignment OS use — one lookup per new company)  
**Logo API:** Free up to 500,000 requests/month  

**Response structure:**
```json
{
  "colors": [
    {"hex": "#EC5B24", "type": "primary"},
    {"hex": "#1B1B1B", "type": "secondary"}
  ],
  "fonts": [{"name": "Inter", "type": "body"}],
  "logos": [{"theme": "light", "formats": [...]}]
}
```

**Rate limit strategy:** Cache aggressively in Company_Memory. One API call per company lifetime. Never call on every run.

---

## 43. Fallback Color Hierarchy

| Tier | Source | When Used |
|---|---|---|
| 1 | Company_Memory brand block | Always check first |
| 2 | Brandfetch API | Company_Memory miss or low confidence |
| 3 | Web scraping (homepage CSS/meta) | Brandfetch miss |
| 4 | Assignment OS defaults | All else fails |

**Tier 4 defaults (not navy/blue generic):**
```
brand_primary: "#2C5F8A"       (professional blue)
brand_secondary: "#1A1A2A"     (near-black)
brand_background: "#FFFFFF"    (white)
brand_text: "#1A1A2A"          (near-black)
brand_accent: "#4A9EDB"        (lighter blue)
```

Always set `brand_confidence: "default"` when using Tier 4. Log to state.json.

---

## 44. Company_Memory Brand Caching

Brand block format in Company_Memory.md (written by Context Builder after brand lookup):

```markdown
## Brand Identity
brand_primary: "#EC5B24"
brand_secondary: "#1B1B1B"
brand_tertiary: "#FAC8A5"
brand_background: "#FFFFFF"
brand_text_primary: "#1B1B1B"
brand_text_secondary: "#555555"
brand_confidence: "confirmed"
brand_source: "brandfetch"
brand_retrieved: "2026-07-05"
brand_font_heading: "Inter"
brand_font_body: "Inter"
```

**Context Builder** is responsible for populating this block during its pipeline stage. Formatter reads it passively — no API calls from Formatter.

**Invalidation:** Brand block older than 90 days should be re-verified. State.json tracks `brand_retrieved` date for this purpose.

---

## 45. Color Contrast Validation

Validation runs inside Formatter before generating output. Fails fast with specific error if brand colors violate WCAG AA.

```python
def relative_luminance(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    def channel(c):
        c = c / 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)

def contrast_ratio(color1, color2):
    l1 = relative_luminance(color1)
    l2 = relative_luminance(color2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

# Validate text-on-background
ratio = contrast_ratio(brand['text_primary'], brand['background'])
assert ratio >= 4.5, f"Text contrast {ratio:.1f}:1 fails WCAG AA (need 4.5:1)"

# Validate action title on background
ratio = contrast_ratio(brand['text_primary'], brand['background'])
# Action title is --text-title size (1.8rem+) → 3:1 threshold
assert ratio >= 3.0, f"Large text contrast {ratio:.1f}:1 fails WCAG AA"
```

If validation fails: auto-adjust `text_primary` to #000000 or #FFFFFF (whichever achieves passing ratio). Log adjustment. Continue generation — do not fail pipeline.

---

# Part VI — Quality Assurance Architecture

## 46. Visual QA Agent Contract

Visual QA runs AFTER Formatter completes. One QA instance per output format. QA has no knowledge of how the deck was built — reads only the output file.

**Contract:**
- Input: path to output file (HTML or PPTX)
- Input: `draft.json` (to verify slide count and types)
- Input: brand block from Company_Memory
- Output: `qa_report.json` with per-check results

**QA failure routing:**
- QA failures → Formatter revision (NOT a Checker loop)
- Checker loop only triggered by structural content failures (wrong recommendation, missing evidence)
- QA failures are presentational: missing slide, wrong color, broken layout

---

## 47. HTML QA Checklist

Binary pass/fail for each item. ALL must pass. No exceptions.

1. File is single HTML file (no external references except Mermaid/Chart.js CDN)
2. File opens without errors in browser (no console errors on load)
3. Slide count matches `draft.json` slide count exactly
4. All slides have `data-type` attribute matching one of 12 canonical types
5. All slides have `100dvh` height (no scrollbar visible)
6. No slide allows overflow scroll (`overflow: hidden` verified)
7. Action title present on every non-title slide (not just a topic label — must be sentence)
8. Brand primary color applied to accent elements (verified via computed style)
9. Text-on-background contrast ≥ 4.5:1 (checked programmatically)
10. No hardcoded hex colors in CSS (all must use `var(--color-*)`)
11. Font sizes all using `clamp()` (no fixed px/rem outside `:root` token block)
12. Keyboard navigation works (ArrowRight advances, ArrowLeft retreats)
13. Dot indicators present and count matches slide count
14. `prefers-reduced-motion` media query present in CSS
15. All images have `alt` attributes
16. Speaker notes present in `<aside>` elements where `draft.json` includes notes
17. No prev/next button elements (dots only)
18. No CDN references except allowed Mermaid and Chart.js
19. Slide counter visible (`N / M` format)
20. No cream/beige backgrounds (background must be white or `--color-surface`)
21. Bullet count per slide ≤ 5
22. File size ≤ 2MB (larger suggests bloated base64 images)

---

## 48. PPTX QA Checklist

1. File opens without error in PowerPoint/LibreOffice Impress
2. Slide count matches `draft.json` slide count
3. All slides use named layouts from template (not blank layouts)
4. Action title present on every slide as proper title placeholder (idx=0)
5. Brand primary color applied to title text or accent shapes
6. Font is Calibri or Arial throughout (no missing font warnings)
7. All images render (no broken image placeholders)
8. Speaker notes present on all slides where `draft.json` includes notes
9. No text overflow (no text cut off by shape boundaries)
10. Slide master is consistent across all slides (single master)
11. All text boxes have non-zero width and height
12. Color values are explicit RGB (not "auto" or theme references that break on different machines)
13. No empty slides
14. Chart data is embedded (not linked to external files)
15. File size ≤ 10MB
16. No placeholder text ("Click to add title", "[INSERT CONTENT]")
17. Source citations present on data slides
18. Presentation properties set: Title, Author metadata

---

## 49. Accessibility QA Checklist

Applies to HTML track only (PPTX accessibility tooling is limited).

1. All slides have `role="region"` or equivalent ARIA landmark
2. `<h1>` or `role="heading"` present for action title
3. Image alt text is descriptive (not empty, not "image")
4. Color is not sole carrier of meaning (shapes/labels used alongside color)
5. Focus order follows visual order (tab key traversal)
6. Slide navigation is keyboard-operable
7. `prefers-reduced-motion` disables CSS transitions when set
8. Font sizes scale with browser zoom (no fixed pixel sizes)
9. Sufficient contrast for all text elements (≥ 4.5:1 for body, ≥ 3:1 for large)
10. Speaker notes provide text equivalent of visual-only information

---

## 50. QA Failure Routing

```
qa_report.json
├── html_qa_results: { check_id: pass|fail, ... }
├── pptx_qa_results: { check_id: pass|fail, ... }
├── accessibility_results: { check_id: pass|fail, ... }
├── overall_verdict: "PASS" | "FAIL"
└── failures: [{ check_id, description, fix_instruction }]
```

**On FAIL:** Orchestrator sends `fix_instruction` list to Formatter with specific corrections. Formatter re-runs targeted fixes (not full regeneration). QA re-runs on corrected output. Max 2 QA correction loops before HITL escalation.

**QA loops ≠ Checker loops.** State.json tracks them separately. QA loop count does not increment `loop_count` (Checker gate).

---

# Part VII — Token Budget and Performance

## 51. Token Budget Strategy

Formatter is token-light by design. It reads only:

| Input | Approx Tokens |
|---|---|
| draft.json (typical) | 2,000-4,000 |
| Skill file (deck-builder.md) | 3,000-5,000 |
| Company_Memory brand block | 200-400 |
| Total Formatter context | 5,200-9,400 |

This is intentional. Formatter must NOT read workspace/*.md files, research files, or WORKSPACE.md. Those were consumed by Case Builder. Formatter's job is rendering, not comprehension.

**Optimization:** draft.json includes `slide_type` already set by Case Builder. Formatter maps type to template — no reasoning required about what type to use.

---

## 52. Agent Context Contracts

| Agent | Reads | Does NOT Read |
|---|---|---|
| Formatter (HTML) | draft.json, Company_Memory brand block, deck-builder.md skill | workspace/*.md, research files, WORKSPACE.md |
| Formatter (PPTX) | draft.json, Company_Memory brand block, pptx-builder.md skill | workspace/*.md, research files, WORKSPACE.md |
| Visual QA | Output file, draft.json, Company_Memory brand block | draft construction history |

These contracts are enforced by CLAUDE.md rule: "Agents never load full WORKSPACE.md." Formatter is a pure renderer, not a reasoning agent.

---

## 53. Multi-Format Parallelism

When both HTML and PPTX requested:

```
state.json: output_formats: ["html", "pptx"]

Orchestrator spawns:
├── Agent: Formatter (HTML) → async
└── Agent: Formatter (PPTX) → async

Both complete → 

Orchestrator spawns:
├── Agent: Visual QA (HTML) → async
└── Agent: Visual QA (PPTX) → async

Both QA pass → state.json: status: "complete"
```

No sequential dependency between formats. Both formatters read the same draft.json independently.

---

## 54. Caching Strategy

**Brand colors:** Cached in Company_Memory. Lifetime: 90 days. Never re-fetched within lifetime.

**HTML template strings:** Formatter includes templates as inline strings in skill file — no disk reads. Templates for all 12 slide types embedded in deck-builder.md skill.

**PPTX template file:** `Global/templates/assignment-os-base.pptx` read once per Formatter run. Not regenerated per slide.

**Chart exports:** If chart images need to be shared between HTML and PPTX tracks, saved to `workspace/charts/` by HTML Formatter, read by PPTX Formatter. Requires sequential (not parallel) execution when chart sharing needed. Default: each track generates independently.

---

## 55. Error Recovery

**Missing brand colors:** Use Tier 4 defaults. Log to state.json. Continue generation. Do not halt pipeline.

**Brandfetch API failure:** Fall through to web scraping (Tier 3). If also fails, use Tier 4 defaults.

**Mermaid CDN unavailable (HTML):** Degrade gracefully — show diagram source code in `<pre>` block. QA check #18 (CDN references) has exception for Mermaid — this check verifies Mermaid CDN is used, not blocked.

**python-pptx unavailable:** Fall back to PptxGenJS. Notify in QA report.

**Content overflow (slide too full):** Log as QA warning. Formatter attempts auto-split if overflow > 20%. User notified in QA report.

**QA loop limit exceeded:** HITL escalation. Show user specific failing checks. User makes decision on acceptable exceptions (e.g., brand color contrast fails because brand is light orange — user may accept this).

---

# Part VIII — Skill File Specifications

## 56. deck-builder.md v1 — Full Specification

Key additions over v0:

1. **SKILL.md frontmatter** — proper `name`, `description`, `version`, `model`, `allowed-tools`, `user-invokable: false`
2. **Design token injection** — reads brand block, generates `:root { ... }` token block at render time
3. **12 slide type templates** — all 12 types specified, not just 7
4. **clamp() enforcement** — explicit rule: all font sizes must use clamp(), max ≥ 2× min
5. **100dvh pairing** — explicit rule: always pair `height: 100vh` with `height: 100dvh`
6. **Mermaid CDN allowed** — explicit exception to no-CDN rule for diagram content
7. **Chart.js CDN allowed** — explicit exception for chart rendering
8. **Speaker notes pattern** — `<aside class="speaker-notes">` inside each `<section>`
9. **Accessibility requirements** — ARIA, alt text, focus indicators, reduced-motion
10. **Anti-patterns list** — 16 explicit prohibitions
11. **QA checklist reference** — skill instructs Formatter to run self-check before writing output
12. **Print CSS** — complete `@media print` block for PDF export

**Structural changes:**
- Step 0 (Brand Color Search) renamed to "Brand Token Injection" — reads Company_Memory first, only searches if cache miss
- Dot indicators required (was already required in v0, now explicitly specified in template)
- Section Divider slide type added (was absent in v0)
- Process/Flowchart slide type added
- Quote/Principle slide type added
- Two-Column slide type added

---

## 57. pptx-builder.md v1 — Full Specification

New skill (no v0 equivalent in deck-builder.md).

**Key specifications:**

1. **Frontmatter** — `name: pptx-builder`, proper required fields
2. **Template-first approach** — load `Global/templates/assignment-os-base.pptx`, never build from scratch
3. **12 layout mappings** — each draft.json `slide_type` maps to named PPTX layout
4. **Placeholder population** — use idx-based access, not positional
5. **Brand color application** — RGB values from Company_Memory brand block
6. **Font specification** — Calibri for PPTX (cross-platform safe)
7. **Speaker notes** — python-pptx notes_slide pattern
8. **Image handling** — add_picture() with correct position/size
9. **Chart export** — puppeteer screenshot for Chart.js charts before embedding
10. **QA pre-check** — validate output before writing (check placeholder fill, no empty slides)
11. **Error handling** — specific fallback for each failure mode

---

## 58. brand-templates.md v1 — Updated Specification

**Retained from v0:**
- File naming convention: `Company_AssignmentType_YYYY-MM-DD.[format]`
- Color palette structure

**Changed from v0:**
- Remove all reveal.js CDN references (superseded)
- Remove HTML template section (now owned by deck-builder.md)
- Change default colors from navy (#1A1A2E, #16213E, #0F3460) to Assignment OS defaults (#2C5F8A, #1A1A2A, #4A9EDB)
- Add Brandfetch as primary color source
- Add Company_Memory brand caching protocol
- Expand PPTX templates to match 12-type taxonomy
- Add contrast validation requirement
- Update Visual QA checklist from 8 items to 22 items (HTML) + 18 items (PPTX)

**New in v1:**
- Brand confidence tiers (confirmed, scraped, default)
- 90-day cache invalidation rule
- Cross-format color consistency requirement (HTML and PPTX must use same brand colors)

---

## 59. presentation-checker.md — New Skill

New skill for automated pre-QA validation within Formatter. Runs before Formatter writes output file.

**Purpose:** Catch errors during generation (not after). Reduces QA loop count.

**Checks run by Formatter self-validation:**
- Slide count matches `draft.json`
- All `slide_type` values are in canonical 12-type list
- All action titles are sentences (end with period, length > 20 chars, not topic labels)
- Brand color tokens injected (`:root` block present)
- No hardcoded hex values outside `:root`
- All font sizes use `clamp()`
- Speaker notes `<aside>` present where `draft.json.speaker_notes` is non-empty

Failures abort Formatter, log to state.json with specific error. Formatter retries with corrections. Not counted as QA loop.

---

## 60. Skill Frontmatter Requirements

All Presentation OS skills must include:

```yaml
---
name: [skill-name]              # Required
description: [usage trigger text] # Required — model reads this to decide when to load skill
version: 1.0                    # Recommended
model: claude-sonnet-4-5        # Recommended — sets default model for this skill
allowed-tools: [tool list]      # Recommended — restricts tool access
user-invokable: false           # Required for Formatter/QA agents — prevents direct invocation
---
```

`user-invokable: false` is critical for pipeline agents. Prevents users from accidentally triggering Formatter directly without proper pipeline state.

---

# Part IX — Version 0 Gap Analysis

## 61. deck-builder.md v0 Strengths

- Correct viewport architecture (100vw × 100vh, overflow hidden) — maintained in v1
- Correct dot indicator pattern (prev/next prohibited) — maintained
- CSS variable structure (--bg, --accent, etc.) — extended in v1
- 7 slide type definitions — expanded to 12 in v1
- Self-contained single file requirement — maintained
- Brand color search as Step 0 — formalized and automated in v1
- No CDN for layout/style — maintained
- Anti-pattern list (5 items) — expanded to 16 items in v1
- Keyboard navigation (Left/Right) — expanded to include Space, N for notes, touch swipe

---

## 62. deck-builder.md v0 Weaknesses

1. **No 100dvh pairing** — iOS Safari 100vh bug not addressed
2. **No clamp() requirement** — fixed font sizes allowed, violates accessibility
3. **No design token naming convention** — `--bg`, `--accent` too generic for 12-slide-type system
4. **No brand caching protocol** — runs brand search every invocation (redundant API calls)
5. **No SKILL.md frontmatter** — skill not properly structured for Claude Code skill system
6. **7 slide types only** — missing Section Divider, Process/Flowchart, Quote/Principle, Two-Column, Comparison
7. **No Mermaid integration** — diagrams must be built with CSS only
8. **No Chart.js integration** — no automated charting
9. **No speaker notes pattern** — notes not addressed
10. **No print CSS** — no PDF export path
11. **No contrast validation** — brand colors may fail WCAG AA
12. **No self-check before output** — formatting errors caught late by QA only
13. **No accessibility requirements** — ARIA, alt text, reduced-motion not specified

---

## 63. brand-templates.md v0 Strengths

- Establishes file naming convention (retained in v1)
- Defines PPTX template concept (expanded in v1)
- Includes basic Visual QA checklist (8 items, expanded to 22+18 in v1)

---

## 64. brand-templates.md v0 Weaknesses

1. **reveal.js CDN reference** — already superseded by deck-builder.md but file still contains it
2. **Default colors are generic** — navy/blue palette signals "template" not "brand"
3. **No Brandfetch integration** — manual color search only
4. **No Company_Memory caching** — re-searches every session
5. **PPTX templates underspecified** — 6 types defined, 5 fewer than v1 taxonomy
6. **QA checklist too short** — 8 items catch only obvious failures
7. **No contrast validation** — accepted any brand colors without accessibility check
8. **No cross-format consistency requirement** — HTML and PPTX could diverge in color

---

## 65. Migration Path from v0 to v1

**Phase 1 (immediate):** Update brand-templates.md to remove reveal.js CDN references. Change default colors. Add Brandfetch reference. These changes are backwards-compatible.

**Phase 2 (week 2):** Deploy deck-builder.md v1 with full token system and 12 slide types. Existing presentations regenerated on next Formatter run.

**Phase 3 (week 3):** Deploy pptx-builder.md v1. Test with 3 company assignments.

**Phase 4 (week 4):** Deploy presentation-checker.md. Enable QA 22-point checklist.

**No breaking changes to upstream agents.** draft.json format unchanged. Formatter contract unchanged (reads draft.json, writes to OUTPUTS/).

---

# Part X — Implementation Roadmap

## 66. Phase 1: Foundation (Week 1)

**Deliverables:**
1. Update `brand-templates.md` — remove CDN, update defaults, add Brandfetch
2. Create `Global/templates/assignment-os-base.pptx` — 12-layout template
3. Add brand block to Company_Memory format documentation
4. Update AGENT_CONTRACTS.md with Formatter/QA contracts
5. Create `Global/skills/presentation-checker.md`

**Success criteria:** Context Builder successfully populates brand block in Company_Memory. Brand block format validated on 3 existing company folders.

---

## 67. Phase 2: HTML Track (Week 2)

**Deliverables:**
1. Rewrite `Global/skills/deck-builder.md` to v1 spec
2. All 12 slide type templates implemented inline
3. CSS token system with brand injection
4. Mermaid + Chart.js integration examples
5. Print CSS for PDF export
6. 22-point QA checklist implemented

**Success criteria:** Formatter generates valid HTML for all 12 slide types. QA checklist passes on test deck. PDF export via browser print produces clean output.

---

## 68. Phase 3: PPTX Track (Week 3)

**Deliverables:**
1. Create `Global/skills/pptx-builder.md` v1
2. Python script `Global/scripts/pptx_builder.py` (invoked via Bash)
3. Layout-to-type mapping for all 12 types
4. Brand color application via RGBColor
5. Speaker notes population
6. 18-point QA checklist implemented for PPTX

**Success criteria:** Formatter generates valid PPTX that opens in PowerPoint without warnings. All 12 slide types render correctly. Speaker notes present.

---

## 69. Phase 4: QA Integration (Week 4)

**Deliverables:**
1. Update Visual QA agent contract with full checklist references
2. QA failure routing logic in Orchestrator
3. QA loop counter separate from Checker loop counter in state.json
4. Test suite: 5 assignments run end-to-end, QA pass rate measured
5. HITL escalation path for QA loop limit

**Success criteria:** QA catches all 22 HTML checks and 18 PPTX checks. QA failures route to Formatter revision (not Checker loop). HITL triggered correctly when loop limit hit.

---

## 70. Final Recommendations

### Architecture Summary

The Presentation OS Version 1 represents a significant upgrade over Version 0 in six areas:

1. **Brand persistence** — Brandfetch + Company_Memory caching eliminates redundant API calls and ensures color consistency across all assignments for a company.

2. **Design token system** — CSS custom properties with semantic naming enables brand-swapping without template changes. All 12 slide types share the same token hierarchy.

3. **Dual-track rendering** — HTML primary, PPTX secondary. Parallel execution when both requested. Identical brand colors across formats.

4. **Comprehensive slide taxonomy** — 12 canonical types covering all consulting deliverable needs. draft.json `slide_type` field drives template selection — no reasoning required at render time.

5. **Quality gate architecture** — 22-point HTML QA + 18-point PPTX QA + 10-point accessibility QA. Binary pass/fail. QA failures route to Formatter revision, not Checker loop (preserving loop count budget).

6. **Token efficiency** — Formatter reads only draft.json (~3k tokens). Brand lookup cached. Total Formatter context under 10k tokens per run.

### Key Principles to Enforce

- **Pyramid Principle above all.** Every slide must have an action title. Topic labels are rejected by QA check #7. Case Builder must write sentences, not labels.
- **Data-ink ratio.** Chartjunk is prohibited. Every visual element serves communication. Diagrams replace bullets when relationship matters.
- **Brand fidelity.** The same Ixigo orange (#EC5B24) that appears on the hiring company's website appears on slide 1, slide 7, and the PPTX version. No drift.
- **Single-file constraint.** HTML output is one file. Email-safe. Always works. CDN failures cannot break a submitted deliverable (Mermaid/Chart.js are graceful degradation risks, not blocking dependencies).
- **QA loops are not Checker loops.** Presentational failures are fixed by Formatter in a tight loop. Content failures require Checker involvement. Preserving this distinction keeps the 2-loop cap meaningful.

### One Decision to Revisit

The Mermaid/Chart.js CDN exception introduces a failure mode. If both CDNs are unavailable at review time, diagrams and charts fail silently or show errors. Consider: (1) always including Mermaid and Chart.js as inline bundled JavaScript (increases file size by ~300KB), or (2) accepting CDN risk for charts/diagrams only (layout/style remains CDN-free). Recommendation: accept CDN risk for diagrams/charts, require inline fallback `<noscript>` or `<pre>` display of diagram source. This gives reviewer the data even if rendering fails.

### Skill Files to Create/Update

| File | Action | Priority |
|---|---|---|
| `Global/skills/deck-builder.md` | Major rewrite to v1 spec | P0 |
| `Global/skills/brand-templates.md` | Update to v1 spec | P0 |
| `Global/skills/pptx-builder.md` | Create new | P1 |
| `Global/skills/presentation-checker.md` | Create new | P1 |
| `Global/templates/assignment-os-base.pptx` | Create new | P1 |
| `Global/scripts/pptx_builder.py` | Create new | P1 |

---

*Document complete. 70 sections. Covers all research areas, answers all 8 key design questions, provides complete implementation specifications for Version 1 Presentation OS.*

*Next step: Update deck-builder.md and brand-templates.md to implement Phase 1 and Phase 2 specifications.*
