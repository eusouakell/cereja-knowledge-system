# Chama motion system

Motion is a brand layer and an interaction layer.

The desired quality is **confident, editorial and alive**. The user-selected Jeleiz reference is useful particularly for its visible motion personality. 60fps.design and 21st.dev are pattern libraries for studying how motion behaves across real interfaces.

## Motion principles

### Move with editorial intent

A reveal should help a reader enter a story, understand sequence or notice a relationship.

### One dominant movement at a time

Several large animations competing on the same viewport create noise and cognitive load.

### Prefer choreography over spectacle

A few coordinated elements are stronger than every element animating independently.

### Motion must survive removal

If reduced motion is enabled, the experience must remain complete and understandable.

### Interactive feedback is faster than editorial motion

Buttons and controls should respond quickly. Storytelling sequences can breathe.

## Motion tokens

Initial proposed scale:

| Token | Duration | Intended use |
|---|---:|---|
| `motion.instant` | 80–120ms | pressed/active feedback |
| `motion.fast` | 160ms | hover, simple state change |
| `motion.standard` | 220ms | nav, card, reveal |
| `motion.editorial` | 420ms | headline/media entrance |
| `motion.story` | 600ms | coordinated hero/section transition |

Avoid interaction-blocking animation beyond this range.

### Easing

Default:

```css
--ease-standard: cubic-bezier(.2,.7,.2,1);
```

Additional easings must have a named behavioral purpose such as `enter`, `exit`, `spring-soft`, not "cool-1".

## Approved motion families

- fade + slight translate;
- mask/reveal for major editorial imagery;
- staggered type or metadata entrance, sparingly;
- shared-element transition when spatial continuity matters;
- hover/tap response;
- number/issue ticker;
- controlled marquee only for non-essential content;
- subtle ambient background movement when it does not reduce reading clarity.

## Avoid by default

- continuous parallax behind long-form text;
- scroll-jacking;
- mandatory horizontal scroll narratives;
- looping attention grabs near body copy;
- flashing;
- high-amplitude scale effects on every hover;
- motion that shifts layout after the user starts reading.

## Reduced motion contract

When `prefers-reduced-motion: reduce`:

- remove large spatial travel;
- remove parallax;
- remove continuous ambient loops;
- remove stagger delays that slow access;
- keep essential state changes, using immediate or opacity-based transitions;
- never hide information that was only reachable through animation.

## Motion review questions

- What job is the motion doing?
- Does it clarify hierarchy or relationship?
- Can the reader ignore it and continue reading?
- Is the interaction response immediate enough?
- Does reduced-motion preserve all meaning?
- Does the animation still look intentional at low-end device performance?
