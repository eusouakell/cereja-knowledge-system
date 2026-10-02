# Flame foundations & tokens

Status: v0.1.

## Token hierarchy

```text
RAW OBSERVATION
      ↓
BRAND FOUNDATION
      ↓
SEMANTIC TOKEN
      ↓
COMPONENT TOKEN (only when necessary)
```

Agents and components should consume semantic roles.

## Color

### Current observed brand foundations

```css
--flame-brand-cherry: #EA1945;
--flame-action-cherry: #BE1035;
--flame-brand-lime: #D7E25B;
--flame-ink: #3A3A3A;
--flame-white: #FFFFFF;
```

### Semantic roles

```css
--color-canvas: var(--flame-white);
--color-surface-primary: var(--flame-white);
--color-text-primary: var(--flame-ink);
--color-text-on-action: var(--flame-white);
--color-action-primary: var(--flame-action-cherry);
--color-accent-signature: var(--flame-brand-cherry);
--color-accent-electric: var(--flame-brand-lime);
--color-focus: var(--flame-brand-cherry);
```

Neutral, state and dark-mode palettes are **not canonical yet**. Add them through reviewed design work rather than inventing a large scale in advance.

## Typography roles

Canonical font families: **pending recovery/approval of the original brand font kit**.

Role behavior is canonical now:

| Token | Purpose |
|---|---|
| `type.display.xl` | hero / issue cover |
| `type.display.lg` | major story title |
| `type.heading.md` | section title |
| `type.heading.sm` | card title |
| `type.body.lg` | lead / standfirst |
| `type.body.md` | default reading |
| `type.body.sm` | secondary explanation |
| `type.meta` | dates, issue IDs, taxonomy |
| `type.ui` | controls |

Use fluid sizing with `clamp()` where it improves responsiveness.

## Spacing

Use a 4px base with semantic aliases.

```text
2  = 0.5rem? no — raw 2px only when optically required
4  = 4px
8  = 8px
12 = 12px
16 = 16px
24 = 24px
32 = 32px
48 = 48px
64 = 64px
96 = 96px
128 = 128px
```

Semantic roles:

- `space.inline.xs`
- `space.inline.sm`
- `space.stack.sm`
- `space.stack.md`
- `space.stack.lg`
- `space.section.md`
- `space.section.lg`

Do not let every component create its own one-off spacing values.

## Grid

Initial rules:

- max editorial canvas: approximately 1280px unless a full-bleed pattern is intentional;
- readable long-form measure: approximately 60–75 characters;
- grid may be asymmetric at desktop;
- collapse order is part of component specification;
- full-bleed and broken-grid moments should remain exceptions.

## Radius

Flame should feel graphic rather than soft.

Proposed roles:

```text
radius.none = 0
radius.sm   = 2–4px
radius.md   = 8px
radius.pill = 999px
```

Use `radius.pill` for tags/chips/status, not as a global default.

## Borders

Prefer clear 1px structural borders and strong top rules for editorial grouping.

Examples:

- issue list separator;
- reference frame;
- story rule;
- focus state;
- data/table boundary.

## Motion tokens

See [motion.md](motion.md). No component should hard-code its own arbitrary easing/duration unless the exception is documented.
