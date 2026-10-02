# Cereja Knowledge System

Canonical knowledge base for Cereja Flamejante.

The system now has a name: **Núcleo**.

Núcleo is the semantic source of truth for what Cereja knows, believes, has evidenced, has published and is still testing. Its companion visual system is **Chama**, documented under [brand/chama](brand/chama/README.md).

```text
NÚCLEO
meaning · evidence · voice · thesis
        +
CHAMA
visual language · interaction · accessibility
        ↓
CEREJA EDITORIAL ENGINE
context routing · composition · gates · human approval
```

## Knowledge architecture

```text
SPEC
→ CONCEPTS
→ DECISIONS + EVIDENCE
→ THESIS STATE
→ VIEWS
→ APPLICATIONS
```

Domains:

```text
brand/
worldview/
editorial/
audience/
thesis-graph/
evidence/
benchmarks/
consulting/
offers/
projects/
archive/
governance/
```

A published newsletter is historical evidence, not automatically current truth.
A benchmark is external reference material, not Cereja strategy.
An external skill is an execution asset, not canonical authority.

## Release status

v0.2 expands the canonical system with:

- named systems: **Núcleo** and **Chama**;
- Chama v0.1: principles, agent-readable DESIGN.md, tokens, motion, components, accessibility and QA;
- an explicit [skills curation](governance/skills-curation.md);
- a [Little Plains Agentic Brand Systems benchmark](benchmarks/little-plains-agentic-brand-systems.md).

These are system contracts under active validation. Chama does not yet claim a complete production component library, and Núcleo does not claim that all historical material has been ingested or revalidated.

## Start here

- [System specification](SYSTEM-SPEC.md)
- [Núcleo + Chama](brand/systems.md)
- [Chama Design System](brand/chama/README.md)
- [Chama agent contract](brand/chama/DESIGN.md)
- [Skills curation](governance/skills-curation.md)
- [Domain model](governance/domain-model.md)
- [Editorial architecture](editorial/editorial-architecture.md)
- [Thesis template](thesis-graph/template.md)
- [Evidence schema](evidence/schema.md)

## Public evidence and companion workflow

Start with the [five-issue public inventory](archive/public-inventory.md), [source authority record](evidence/CF-027.md) and [provisional voice observations](editorial/voice-observations.md). Metadata indexing and a small body-reviewed sample are available; broader external claim validation remains pending.

Execution design lives in [Cereja Editorial Engine](https://github.com/eusouakell/cereja-editorial-engine). Kell owns this project; the published archive remains historical evidence, not automatically canonical knowledge.
