# Flame accessibility baseline

Production target: **WCAG 2.2 AA** as the minimum baseline.

Accessibility is broader than formal conformance and broader than screen-reader compatibility. Flame should support different ways of seeing, hearing, understanding and operating an interface while preserving meaning, agency and task completion.

## Accessibility dimensions

Flame reviews at least these dimensions:

- **visual** — contrast, low vision, color-vision differences, text scaling, zoom and reflow;
- **non-visual** — semantic structure, screen-reader navigation, names, roles, states and alternatives to visual media;
- **motor** — keyboard operation, target size, no precision-only gestures, predictable focus and alternatives to drag/hover;
- **vestibular / motion** — reduced motion, no essential parallax or movement dependency, no unnecessary continuous animation;
- **cognitive** — clear hierarchy, stable navigation, manageable density, understandable labels, error prevention and recovery;
- **auditory** — captions/transcripts when audio or video carries information; no audio-only essential instruction;
- **language / comprehension** — plain interaction language, meaningful labels, no decorative jargon in task-critical UI.

This list is an operating lens, not a claim to cover every disability or assistive-technology scenario.

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

Screen-reader support is one accessibility mode within the broader Flame baseline. It is documented separately because highly visual, motion-rich editorial interfaces create specific semantic risks.

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


## Cognitive and sensory accessibility guardrails

Flame's visual performance has a ceiling: **expressiveness stops where distraction, overload or loss of control begins**.

This is especially important for people with attention differences, autism, dyslexia and other cognitive/learning differences.

External guidance used as references:

- **GAIA** — open recommendations for accessible interfaces with focus on autism:
  https://gaia.wiki.br/
- **.horcel** — inclusive-design recommendations focused on ADHD, dyslexia, dyscalculia and dysorthography:
  https://horcel.wiki.br/
- **W3C COGA — Making Content Usable for People with Cognitive and Learning Disabilities**:
  https://www.w3.org/TR/coga-usable/

These are complementary references. WCAG 2.2 AA remains the baseline conformance target; GAIA, .horcel and COGA help cover cognitive and learning needs that a WCAG checklist alone may not surface.

### Stimulation budget

A page or component should not maximize every expressive dimension at once.

Avoid combinations such as:

- multiple simultaneous moving regions;
- high-contrast animation + dense text + changing background;
- several competing hover effects near long-form reading;
- auto-playing media beside task-critical content;
- persistent movement that cannot be paused;
- frequent layout shifts that force re-orientation.

Prefer:

- one dominant animated idea per viewport/section;
- generous quiet areas between expressive moments;
- stable reading surfaces;
- clear hierarchy and whitespace;
- user control over non-essential movement;
- a low-stimulation or reading mode when a surface genuinely benefits from heavy art direction.

### Attention and predictability

- do not use animation merely to keep attention;
- do not interrupt reading with unrelated motion;
- preserve consistent component behavior;
- make navigation and next steps predictable;
- keep consequences of actions explicit;
- provide recovery cues when users lose context;
- avoid requiring users to remember hidden state or instructions.

### Autism-informed considerations

From GAIA's direction, Flame should especially preserve:

- simple, understandable visual/textual vocabulary;
- consistent navigation and layout;
- control over distracting elements;
- clear grouping and whitespace;
- optional customization where it materially improves comfort;
- multiple representations without forcing all representations at once.

### ADHD / learning-difference-informed considerations

From .horcel's direction, Flame should especially preserve:

- clear typographic hierarchy;
- shorter readable line lengths for long-form content;
- left-aligned body text by default;
- logical grouping and spacing;
- concise, clearly signposted sections;
- predictable patterns;
- explicit instructions and feedback;
- reduced working-memory burden.

### Validation rule

An interface can pass automated accessibility tests and still fail Flame if users with cognitive or learning differences cannot comfortably understand, focus on, recover within or complete the experience.

For high-impact surfaces, include real-user or representative usability testing rather than relying only on automation.
