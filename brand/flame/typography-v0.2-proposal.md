# Flame typography — v0.2 proposal

Status: **proposal — pending Kell approval before becoming canonical**.

Owner: Flame / Editorial Typography Director.

This proposal turns Flame's existing typographic intent into an explicit system **without selecting a new canonical typeface**.

The current website fallbacks remain implementation facts:

- display: Georgia / Times New Roman / serif;
- body/UI: Arial / Helvetica / sans-serif.

They are not promoted here as the final brand families.

## 1. Purpose

Typography should create editorial rhythm while preserving:

- long-form reading comfort;
- clear hierarchy;
- responsive stability;
- Portuguese and English diacritics;
- accessible zoom/reflow;
- predictable UI behavior;
- cross-medium continuity.

The system should feel like an independent digital publication, not a dashboard with decorative headlines.

## 2. Semantic roles

| Role | Job | Default behavior |
|---|---|---|
| `type.display` | issue/story statements | dramatic scale, tight leading, selective negative tracking |
| `type.heading` | section hierarchy | editorial but more compact/stable than display |
| `type.body` | reading | neutral, highly legible, bounded measure |
| `type.ui` | nav/actions/controls | compact, direct, no display-style compression |
| `type.meta` | issue numbers/dates/tags/provenance | small but deliberate; uppercase only when useful |
| `type.code` | technical fragments | monospace only where semantic |

A component chooses a semantic role. It should not pick a font family ad hoc.

## 3. Current family boundary

Until the original brand font kit is recovered and reviewed:

```css
--font-display: Georgia, "Times New Roman", serif;
--font-body: Arial, Helvetica, sans-serif;
--font-ui: Arial, Helvetica, sans-serif;
--font-meta: Arial, Helvetica, sans-serif;
```

These aliases are **fallback roles**, not a final typeface declaration.

### Guard

A new canonical family requires:

- verified source;
- license/reuse terms;
- Portuguese diacritic coverage;
- web delivery/performance review;
- fallback behavior;
- specimen review;
- Kell approval.

Do not substitute a fashionable typeface simply because it looks editorial.

## 4. Proposed scale

The scale is role-driven rather than a single modular ratio.

### Display

Use fluid size with bounded extremes.

```css
font-size: clamp(3rem, 6vw, 5.25rem);
line-height: 1.00–1.08;
letter-spacing: -0.02em to -0.05em;
```

Use the tighter end only for short headlines.

Longer display copy should relax tracking/leading before shrinking aggressively.

### Section heading

```css
font-size: clamp(2rem, 4vw, 3.5rem);
line-height: 1.05–1.15;
letter-spacing: -0.01em to -0.04em;
```

### Subheading / card heading

Target range:

```text
24–32px
line-height 1.10–1.25
```

Do not compress multi-line headings until accents/descenders visually collide.

### Body

Current web baseline remains a useful reference:

```text
18px / 1.6
```

Recommended operational envelope:

```text
16–21px
line-height 1.50–1.75
measure ~45–75 characters
```

A reading surface should prefer measure/leading adjustments before making body text smaller.

### UI

```text
15–17px
line-height 1.2–1.5
font-weight 600–700 only where control emphasis needs it
```

Controls must remain readable under browser text zoom.

### Metadata

Typical range:

```text
12–14px
line-height 1.3–1.5
tracking 0 to .12em
```

Uppercase is allowed for short labels/eyebrows, not long explanatory strings.

## 5. Responsive behavior

Responsive typography changes hierarchy **without changing semantic order**.

Rules:

1. reduce display scale before reducing body scale;
2. preserve body measure through container width;
3. do not use viewport units without min/max bounds;
4. prevent heading overflow with wrapping, not clipping;
5. avoid fixed-height text containers;
6. verify Portuguese words with accents and long unbroken technical terms;
7. allow metadata to wrap instead of truncating provenance by default.

## 6. Reading rhythm

Preferred editorial sequence:

```text
meta / eyebrow
      ↓
display statement
      ↓
lead
      ↓
body / evidence
      ↓
interruption / quote / data
      ↓
return to reading
```

The display family creates contrast; body typography carries trust and duration.

Do not make every card/headline visually equivalent.

## 7. Tracking rules

Negative tracking is a display tool, not a universal identity effect.

- display: may use `-0.02em` to `-0.05em`;
- headings: use sparingly;
- body: default neutral tracking;
- UI: neutral unless the control style explicitly requires otherwise;
- uppercase metadata: modest positive tracking may improve recognition.

Tracking must be reviewed with accented uppercase Portuguese strings.

## 8. Line breaking

Editorial line breaks may be authored on controlled hero surfaces.

They must not:

- encode meaning unavailable in the text itself;
- require `<br>` on body copy;
- create broken screen-reader names;
- become unreadable after localization or zoom.

Prefer width constraints and balanced wrapping before manual breaks.

## 9. Multilingual and fallback behavior

Current priority languages:

- Portuguese;
- English;
- Spanish when the format requires it.

Any future canonical family must support:

- Latin accents used in Portuguese/Spanish;
- punctuation/quotation behavior;
- numerals needed for issue/date/data presentation.

Fallback switching should not create severe layout shift or hierarchy collapse.

When a font is unavailable, semantic role and hierarchy must survive.

## 10. Webfont performance

If a future canonical webfont is approved:

- load only required families/weights/styles;
- prefer modern webfont formats;
- avoid blocking the first readable render;
- define a deliberate fallback stack;
- review layout shift from font swap;
- do not ship unused display weights merely for completeness.

Performance is part of the type system.

## 11. Accessibility checks

Typography review includes:

- browser text zoom;
- reflow/narrow widths;
- no clipped text;
- no fixed-height text traps;
- readable line measure;
- sufficient text/background contrast;
- links identifiable beyond color when context requires;
- heading hierarchy consistent with semantics.

A visually dramatic display treatment cannot make reading or navigation harder.

## 12. Kinetic-type handoff

When typography moves, Motion Web/Video Director receives:

- semantic text role;
- reading order;
- accessible name requirement;
- allowed split unit (block/line/word);
- no-motion equivalent.

Default for Flame:

> animate line/block groups before individual characters.

Character-level animation needs a specific editorial reason and must preserve a coherent accessible name.

## 13. Promotion gate

This proposal can become canonical `brand/flame/typography.md` only after Kell approves:

- the semantic role model;
- scale/rhythm behavior;
- current fallback boundary;
- future font-approval process.

Approval of this system **does not automatically approve a new font family**.

## 14. Open decision

The original font kit remains unresolved.

Until it is recovered and reviewed, typography should be evaluated on:

- hierarchy;
- measure;
- leading;
- tracking;
- responsive behavior;
- fallback resilience;

not on an invented replacement family.
