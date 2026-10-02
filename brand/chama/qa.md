# Chama QA & governance

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
5. **Motion** — does movement have a job?
6. **Accessibility** — can different users complete the experience?
7. **Identity** — does it feel specifically Cereja?
8. **Implementation** — are tokens/components reused correctly?

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
