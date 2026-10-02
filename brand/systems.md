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

## Chama — Design System

**Chama** is the visual and interaction source of truth.

It answers:

- How should Cereja look and feel?
- How does the brand behave across website, newsletter, Instagram, LinkedIn and future products?
- Which design tokens, components and editorial patterns are canonical?
- How should motion support meaning?
- What accessibility constraints are non-negotiable?
- How should an agent build UI without drifting into generic AI aesthetics?

Chama lives under [brand/chama](chama/README.md).

## Relationship

```text
NÚCLEO
meaning · evidence · voice · thesis
        +
CHAMA
visual language · interaction · accessibility
        ↓
FORMAT / CHANNEL CONTRACT
        ↓
PUBLICATION OR PRODUCT
```

The systems are independent but composable.

Núcleo must not decide layout from content alone.
Chama must not invent meaning or claims from visual needs.

The Cereja Editorial Engine can consume both systems when composing multiformat outputs.
