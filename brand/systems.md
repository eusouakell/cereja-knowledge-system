# Cereja systems

The Cereja Flamejante ecosystem now names its two canonical systems.

## Núcleo — Content & Knowledge System

**Núcleo** is the semantic source of truth.

It answers:

- What does Cereja know?
- Which source is authoritative?
- What is evidence, interpretation, thesis, decision or historical publication?
- What context is relevant to a task?
- What can be reused, and what must be revalidated?

Núcleo is implemented by this repository: `cereja-knowledge-system`.

It includes brand, worldview, editorial architecture, audience, thesis state, evidence, benchmarks, projects and governance.

Núcleo also owns durable, brand-neutral-in-wording [Experience Design Principles](experience-design-principles.md). They define the usability, information-architecture, interaction, accessibility and verification baseline that Flame instantiates for Cereja.

## Flame — Design System

**Flame** is the visual and interaction source of truth.

It answers:

- How should Cereja look and feel?
- How does the brand behave across website, newsletter, Instagram, LinkedIn and future products?
- Which design tokens, components and editorial patterns are canonical?
- How should motion support meaning?
- What accessibility constraints are non-negotiable?
- How should an agent build UI without drifting into generic AI aesthetics?

Flame lives under [brand/flame](flame/README.md). Its [experience contract](flame/experience.md) is the Cereja-specific instantiation of the Núcleo experience canon.

## Relationship

```text
NÚCLEO
meaning · evidence · voice · thesis
+ durable experience principles
        ↓
FLAME
brand · visual language · interaction · accessibility
        ↓
SURFACE / FORMAT / PLATFORM CONTRACT
        ↓
PROJECT OR TASK ARTIFACT
        ↓
PUBLICATION OR PRODUCT
```

The systems are independent but composable.

Núcleo must not decide layout from content alone.
Flame must not invent meaning or claims from visual needs.

The Cereja Editorial Engine can consume both systems when composing multiformat outputs.


## Progressive disclosure

The hierarchy is also a context-loading rule.

An agent should read only the layers needed for the current task. A social asset does not need every transactional interaction rule; an app flow should not rely only on visual-brand guidance. Project artifacts inherit upstream authority and should not reopen already approved decisions unless they expose a conflict.
