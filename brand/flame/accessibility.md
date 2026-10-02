# Flame accessibility baseline

Production target: **WCAG 2.2 AA** as the minimum baseline.

Accessibility is also broader than formal conformance: Flame should support reading clarity, cognitive predictability and user control.

## Contrast

- normal text: target at least 4.5:1;
- large text: target at least 3:1;
- interactive component boundaries/states: target at least 3:1 where required;
- never use color as the only state indicator.

Known current decision:

`#EA1945` with white normal text is not the default action pairing. Use `#BE1035` for text-bearing primary action surfaces.

## Keyboard and focus

- all interactive elements keyboard operable;
- visible focus never removed without a replacement;
- logical focus order follows reading/task order;
- skip-to-content remains part of web shell;
- modal/drawer focus must be managed.

## Target size

Aim for at least 44×44 CSS px for primary touch interactions unless the text/link context provides an equivalent accessible target.

## Typography and reading

- body copy must scale without clipping;
- avoid fixed-height text containers;
- avoid overly long line length;
- use clear paragraph spacing;
- headings must preserve semantic nesting;
- metadata must not become illegibly small.

## Zoom and reflow

Pages should remain operable at browser zoom and narrow reflow. Desktop composition cannot assume a fixed viewport.

## Motion

Respect `prefers-reduced-motion`.

See [motion.md](motion.md).

## Images and editorial media

- informative images need meaningful alt text;
- decorative art can use empty alt;
- complex graphics need a textual equivalent or adjacent explanation;
- captions should identify source/context where relevant;
- autoplay video/audio is not a default.

## Cognitive accessibility

Prefer:
- stable navigation;
- clear labels;
- visible state;
- progressive disclosure;
- short UI instructions;
- consistent component behavior.

Avoid:
- surprise navigation;
- ambiguous icon-only actions without accessible labels;
- dense simultaneous motion;
- unnecessary urgency/countdowns;
- interaction that depends on remembering hidden state.

## Accessibility gate

A component is not Flame-ready until its keyboard, focus, contrast, text scaling, responsive and reduced-motion states are specified.


## Screen-reader experience contract

The target is not a fallback. The non-visual experience is a first-class composition.

- landmarks identify major page regions;
- headings form a coherent outline independent of visual scale;
- DOM order follows intended reading and task order;
- visual reordering must not contradict screen-reader sequence;
- controls expose clear accessible names, roles and states;
- decorative animation stays out of the accessibility tree;
- informative illustrations receive concise alt text;
- complex visual stories receive a textual equivalent;
- charts expose the underlying point, scope and source in text;
- meaningful dynamic changes are announced intentionally, not by movement alone;
- focus remains predictable when animated regions enter, leave or reorder.

### Acceptance test

A screen-reader pass should make it possible to answer:

1. Where am I?
2. What is this section about?
3. What changed?
4. What can I do here?
5. What is the relationship between this content and the next?
6. Can I complete the same task without interpreting color, position or animation?

If the visual version communicates information that these questions cannot recover semantically, the design is incomplete.
