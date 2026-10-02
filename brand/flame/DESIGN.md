# FLAME — DESIGN.md

> Agent-readable visual contract for Cereja Flamejante.

Status: v0.1. Read [README.md](README.md) for purpose and limits.

## 1. Visual theme & atmosphere

Cereja Flamejante is a digital editorial brand about **technology, culture, work and the strange things that happen when they meet**.

The interface should feel like an independent magazine designed by someone who understands digital products.

Keywords:

**editorial · curious · sharp · playful · cultured · intelligent · tactile · kinetic · accessible**

Avoid:

- generic startup gradients;
- glassmorphism as default;
- endless rounded cards;
- purple/blue "AI" aesthetics;
- bento layouts used without editorial reason;
- over-smoothing every surface;
- excessive decorative motion;
- copy-heavy cards with identical visual weight;
- visual novelty that reduces legibility.

## 2. Color roles

Use semantic roles. Do not scatter raw hex values through components.

### Core brand

| Role | Value | Use |
|---|---:|---|
| `brand.cherry` | `#EA1945` | signature accent, art direction, large/display moments |
| `action.cherry` | `#BE1035` | accessible button/background/link emphasis |
| `brand.lime` | `#D7E25B` | high-energy contrast, highlights, editorial interruption |
| `text.ink` | `#3A3A3A` | default text |
| `surface.canvas` | `#FFFFFF` | default reading canvas |

### Usage rules

- White normal-size text should not sit on `brand.cherry`; the current measured contrast is below the 4.5:1 target. Use `action.cherry` for text-bearing action surfaces.
- Ink on lime is preferred for readable lime surfaces.
- Brand pink can remain decorative, large-scale or non-textual where contrast requirements differ.
- Never communicate state through color alone.
- New colors require a semantic role and accessibility review before entering the system.

## 3. Typography

Typography should create **editorial rhythm**, not dashboard uniformity.

Semantic roles:

- `type.display` — major story/issue headlines;
- `type.heading` — section hierarchy;
- `type.body` — long-form reading;
- `type.ui` — navigation, buttons, controls;
- `type.meta` — dates, issue numbers, tags, provenance;
- `type.code` — technical fragments when needed.

Current website fallbacks:
- display: Georgia / Times New Roman / serif;
- body and UI: Arial / Helvetica / sans-serif.

These are not yet frozen as canonical brand families. Preserve role behavior until the original brand font files/names are verified.

### Typography behavior

- Display headlines may be large, compressed in line-height and editorially dramatic.
- Body text must optimize reading: comfortable measure, line-height and responsive size.
- Metadata can use tighter spacing and uppercase selectively.
- Do not shrink body copy to "make the layout fit".
- Do not use percentage-based skill bars or decorative typographic scoring.

## 4. Layout

The system uses a disciplined grid with permission for editorial interruption.

Rules:

- reading content should have a bounded measure;
- major editorial sections may break the content grid intentionally;
- asymmetry is allowed when hierarchy remains obvious;
- mobile is a first-class composition, not a stacked desktop afterthought;
- spacing should come from the shared scale;
- repeated cards should not all have identical visual density.

Prefer a strong page rhythm:

```text
quiet → statement → evidence → interruption → reading → invitation
```

## 5. Shape & depth

Default personality is **graphic, not bubbly**.

- Prefer square or low-radius structural surfaces.
- Pills are for tags/status/chips, not every button and container.
- Prefer borders, contrast and layout before shadows.
- Use shadow/elevation only when it communicates layering or interaction.
- Avoid frosted glass as a default visual language.

## 6. Motion philosophy

Motion is part of brand expression.

Use motion to:

1. **orient** — show where an element came from or where it goes;
2. **reveal** — progressively disclose a story or visual;
3. **connect** — relate content across states;
4. **confirm** — acknowledge an action;
5. **delight** — add a limited moment of personality.

Jeleiz is a user-selected reference for the **confidence and presence of animation**, not a visual identity to copy.

60fps.design and 21st.dev are reference libraries for interaction patterns. Rebuild motion using Flame tokens and accessibility rules.

See [motion.md](motion.md).

## 7. Components

Components should expose semantic variants, not arbitrary styling props.

Core owned primitives:

- Button
- TextLink
- Navigation
- Tag
- IssueCard
- FeatureStory
- ReferenceCard
- SignalCard
- QuoteBlock
- DataCallout
- MediaFrame
- SubscribeBlock
- Footer

Editorial organisms:

- IssueHero
- IssueGrid
- CulturalConnection
- SignalSequence
- EvidenceStack
- ReadingList
- VisualMagazineSpread
- ResearchDesk

See [components.md](components.md).

## 8. Accessibility

Baseline: **WCAG 2.2 AA** for production interfaces.

Design and implementation must account for:

- contrast;
- keyboard access;
- visible focus;
- target size;
- reflow and zoom;
- reduced motion;
- text scaling;
- semantic HTML;
- meaningful alternative text;
- non-color cues;
- cognitive clarity.

See [accessibility.md](accessibility.md).

## 9. Responsive behavior

Use content-driven breakpoints rather than device-brand assumptions.

Minimum expectations:

- navigation remains operable without precision pointing;
- editorial display size reduces without losing hierarchy;
- multi-column editorial groups collapse in a deliberate reading order;
- media maintains useful crop/focal point;
- touch targets remain large enough;
- animation never becomes required to understand state;
- horizontal scrolling is reserved for explicitly scrollable media patterns.

## 10. Agent behavior

Before generating or editing UI:

1. read this file;
2. identify the component/pattern being used;
3. use semantic tokens;
4. state any new token/component required;
5. preserve accessibility constraints;
6. use references for pattern inspiration, not visual cloning;
7. run the Flame QA checklist before calling work complete.

If a design request conflicts with Flame, propose the conflict explicitly rather than silently overriding the system.
