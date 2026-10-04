# Flame QA & governance

## Definition of done

A design change is ready for review when:

- it uses semantic tokens;
- it maps to an existing or proposed component/pattern;
- responsive behavior is defined;
- keyboard behavior is known;
- visible focus is present;
- contrast is checked;
- reduced-motion behavior is defined when motion exists;
- content hierarchy remains semantic;
- rights/provenance for editorial media are known;
- visual reference use does not become identity copying.

## Design review

Review in this order:

1. **Intent** — what editorial/product problem is being solved?
2. **Hierarchy** — what should the eye understand first?
3. **Reading** — can the content be consumed comfortably?
4. **Interaction** — are states obvious and predictable?
5. **Motion** — does movement have a job, or is it competing for attention?
6. **Cognitive load** — is the page asking users to process too many simultaneous signals?
7. **Accessibility** — can different users perceive, understand and complete the experience across input/output modes?
8. **Identity** — does it feel specifically Cereja?
9. **Implementation** — are tokens/components reused correctly?

## Agent review

Before accepting agent-generated UI, reject or revise if it introduces:

- arbitrary gradients;
- generic bento sections;
- excessive rounded cards;
- raw hex values instead of roles;
- new fonts without approval;
- unexplained animation libraries/patterns;
- inaccessible hover-only behavior;
- missing responsive/reduced-motion states.

## Visual-delivery controls

For screenshot/design-to-code experiments, use the controls in [visual-delivery/](visual-delivery/README.md).

The order is intentional:

1. visual fidelity is observed by **sensors**;
2. semantic/accessibility invariants are enforced by **deterministic checks** where they are actually machine-verifiable;
3. intent, hierarchy, reading, cognitive load and identity remain **human Flame gates**.

A higher pixel/perceptual similarity score cannot waive a failed semantic or accessibility check.

## Change governance

### Minor change

Variant or token adjustment that does not alter brand semantics.

Requires:
- design review;
- accessibility review.

### System change

New semantic color, typography role, motion family, core component or cross-channel pattern.

Requires:
- rationale;
- affected surfaces;
- migration note;
- Kell approval.

### Reference experiment

Can live as a branch/prototype without becoming canonical.

A successful experiment is promoted only after human review.

## Versioning

- `0.x` — active formation;
- `1.0` — foundations, core components and at least web + one social format validated in real use.

Do not claim a complete design system while typography, component states or real-channel validation remain pending.

## Cognitive-accessibility review

For expressive pages/components, reviewers should explicitly check:

- number of simultaneous attention targets;
- persistent or auto-starting movement;
- visual density around reading/task areas;
- predictability of navigation and controls;
- recovery after distraction;
- working-memory demands;
- clarity of labels/instructions;
- whether a calm/reduced-stimulation treatment is needed;
- whether the experience has been tested with users beyond automated tooling.

A visually impressive result is not Flame-ready if the visual performance makes focus, comprehension or task completion materially harder.


## Distinctiveness

Before calling a visual/product surface Flame-ready, run the [Flame distinctiveness gate](distinctiveness.md). Technical correctness and WCAG checks do not prove that a surface has specific product/brand authorship.
