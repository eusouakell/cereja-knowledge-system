# Screenshot / image-to-HTML — evaluation for Flame

Status: **reference evaluation, not adopted dependency**.

## Question

What should Flame learn from screenshot-to-HTML systems without turning visual similarity into the only definition of quality?

## References reviewed

### sevzq/screenshot-to-html

Source: https://github.com/sevzq/screenshot-to-html

Observed useful pattern:
- render → screenshot → compare → refine loop;
- interaction verification in a real browser;
- hover/focus/click states treated as part of fidelity;
- single-file output as an inspectable artifact.

License observed in the upstream repository: MIT.

**Cereja decision:** borrow the workflow idea, not the source code. No upstream file is copied in this pilot.

### Proximal-Labs/img-to-html

Source: https://github.com/Proximal-Labs/img-to-html

Observed useful research signals:
- pixel similarity alone can be misleading;
- content cropping can make visual comparison more informative;
- DOM/text/layout/color signals can complement raw pixel comparison;
- iterative analyze→fix loops can reduce regression;
- reward functions can be gamed or overfit and therefore require held-out evaluation.

**Cereja decision:** treat this as research input for sensor design only. This review did not establish a reusable code-license boundary, so no code or implementation asset is imported.

## Flame adaptation

The safe control order is:

```text
REFERENCE IMAGE / DESIGN INTENT
          ↓
GUIDE: Flame design language
          ↓
GENERATE / IMPLEMENT
          ↓
VISUAL SENSORS
render · screenshot · diff · layout observations
          ↓
DETERMINISTIC CHECKS
semantics · accessible names · alt · focus · reduced motion
          ↓
HUMAN FLAME GATES
intent · hierarchy · reading · cognitive load · identity
          ↓
APPROVE / REVISE
```

## Sensor, not sovereign score

Visual fidelity metrics may observe:
- pixel/perceptual difference;
- layout displacement;
- typography mismatch;
- color-role mismatch;
- missing/extra visible elements;
- viewport-specific drift.

They must **not** independently approve a surface.

A visually close output can still fail if it:
- turns buttons into clickable divs;
- removes focus treatment;
- loses headings/landmarks;
- lacks alternatives for informative media;
- makes motion essential;
- copies another product's identity too literally.

## Deterministic gates in this pilot

`check_html.py` currently blocks self-contained HTML artifacts when:
- `html[lang]` is missing;
- there is not exactly one `main`;
- no `h1` exists;
- an image lacks an `alt` attribute;
- a link lacks `href` or accessible name;
- a button lacks an accessible name;
- click handlers are attached to non-native generic elements;
- interactive surfaces have no explicit focus style;
- keyframe/animation motion exists without a reduced-motion treatment.

`sensor_html.py` reports, but does not fail on, observations such as heading-level jumps, raw hex count and inline-style count.

## Boundary

This checker is scoped to **self-contained generated HTML artifacts** used in design-to-code experiments. It is not a general web accessibility auditor and does not replace browser testing, axe, screen-reader checks or real-user usability testing.

## Next experimental step

Run the same visual reference through two generation approaches and compare:

1. visual sensor deltas;
2. deterministic gate failures;
3. human Flame review;
4. revision distance to accepted output.

Only then decide whether a screenshot-to-HTML skill belongs in the factory.
