# Cereja skill curation

Status: v0.1.

Skills are external execution assets. They are **not canonical knowledge** and do not override Núcleo, Chama, the Editorial Engine or human approval.

## Selection criteria

A skill enters the curated set when it has a clear job, identifiable provenance and does not duplicate a stronger internal contract.

Evaluate:

- author/upstream;
- scope;
- maintenance/activity;
- license where relevant;
- failure modes;
- what context it needs;
- whether it creates or reviews;
- whether its output can be independently checked.

## Tier A — adopt as active reference / execution aid

### Anthropic Frontend Design
Source: https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design

Role:
- implementation/art-direction aid for distinctive frontend work.

Use when:
- building Chama-based pages/components.

Constraint:
- Chama remains the visual authority; the skill cannot invent the brand.

### Vercel Web Design Guidelines
Source: https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines

Role:
- UI/UX quality review and web implementation checklist.

Use when:
- reviewing a web change before human approval.

Constraint:
- reviewer/gate, not art director.

### Google Stitch Skills
Source: https://github.com/google-labs-code/stitch-skills

Role:
- design-to-code workflows and agent-readable design-system patterns.

Use when:
- prototyping Chama or extracting/structuring design context.

Constraint:
- preserve Cereja provenance and do not treat generated design as canonical automatically.

### getdesign skill / DESIGN.md
Source: https://github.com/MohtashamMurshid/getdesign
Reference catalog: https://github.com/VoltAgent/awesome-design-md

Role:
- extract observable design systems from references;
- compare design-language structure;
- support agent-readable design specs.

Use when:
- analyzing a reference such as Jeleiz;
- checking if Chama is specific enough for agents.

Constraint:
- extraction is evidence about another site's design, not permission to copy its identity.

### Web/app testing skill family
Discovery source: https://skillsclau.de/

Role:
- browser-level UX validation after implementation.

Use when:
- checking responsive flows, navigation, interactive states and regressions.

Constraint:
- tests should be derived from Chama/UX acceptance criteria, not generic "looks good" judgment.

## Tier B — useful specialist / reviewer

### UI UX Pro Max
Source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

Role:
- broad pattern library and UX heuristic reference.

Good for:
- option generation;
- common anti-pattern checks;
- responsive/component ideas.

Do not use as:
- automatic design-system generator that replaces Chama.

### Humanizer
Source: https://github.com/blader/humanizer

Role:
- reviewer for common AI-writing artifacts.

Use as:
- a detector, never as the source of Kell's voice.

Núcleo's approved voice guidance wins.

### Fact Check Skill
Source: https://github.com/petar-nauka/fact-check-skill

Role:
- architectural reference for source evaluation and claim checking.

Use as:
- inspiration for Evidence Gate and verification workflow.

Constraint:
- domain-sensitive claims still require appropriate primary/expert sources.

### Evals Skills
Source: https://github.com/hamelsmu/evals-skills

Role:
- patterns for judge prompts and subjective-quality eval design.

Note:
- the repository is archived, so treat as stable reference material rather than an actively maintained dependency.

Use when:
- formalizing voice, channel-fit or design-quality evals.

## Tier C — discovery only

### skillsclau.de
https://skillsclau.de/

Role:
- radar/catalog.

Do not treat:
- catalog ranking;
- download count;
- category placement

as evidence of skill quality.

Before adoption, trace a skill to its upstream repository or inspect the downloaded contents and provenance.

### 21st.dev / Figcomponents / 60fps / Khroma

These are not canonical Cereja skills.

They are **reference libraries** for UI, Figma components, motion and color exploration. Chama governs what is adopted.

## Internal skills we should create later

External skills cover execution patterns. Cereja-specific judgment should become internal skills only after real use exposes stable rules.

Candidates:

- `chama-ui-review` — checks UI against Chama;
- `chama-motion-review` — purpose + reduced-motion + performance;
- `nucleo-evidence-review` — claim/source/scope;
- `cereja-metapost` — LinkedIn format contract;
- `cereja-visual-magazine` — Instagram format contract;
- `cereja-voice-review` — detects drift without writing "as Kell";
- `editorial-packet-builder` — assembles inspectable packet from Núcleo.

Do not build all of these at once. Promote a workflow into a skill after it has been used and revised manually.
