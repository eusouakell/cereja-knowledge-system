# Fluent 2 × Flame — component coverage audit

Status: **audit / architecture proposal — not yet canonical component API**.

Date: 2026-10-04.

## Why this exists

Fluent 2 was selected as Flame's main UI reference because it already solves expensive design-system problems such as interaction states, accessibility conventions, component anatomy, platform behavior and design-to-code alignment.

The current Flame v0.2 work uses that reference well at the **principle** level, but it does not yet provide enough component coverage to support richer sites and applications.

Current prototype coverage is mostly:

- identity;
- typography/color/shape proposals;
- links/buttons;
- tags;
- images/icons;
- editorial issue cards;
- hero/archive/subscribe compositions;
- visual-magazine/social compositions.

That is enough for a newsletter calling-card and design catalogue.

It is not enough for:

- account/application flows;
- settings;
- complex navigation;
- research tools;
- knowledge interfaces;
- structured forms;
- feedback/error states;
- data-heavy surfaces;
- multi-step agent/product workflows.

## Reference boundary

Primary reference:

- Fluent 2 Web components: https://fluent2.microsoft.design/components/web/react/
  - current React overview reviewed 2026-10-04;
  - 47 components are listed on that overview;
  - Flame distinguishes official Fluent catalogue components from additional product capabilities it may still need.
- Fluent 2 design kits/tokens: https://fluent2.microsoft.design/get-started/design
- Fluent component lifecycle/roadmap: https://fluent2.microsoft.design/component-roadmap/

Flame does **not** automatically copy Fluent's visual identity or implementation library.

For each capability, Flame chooses one of:

- **ADOPT** — behavior/anatomy can stay close to Fluent;
- **ADAPT** — use Fluent's solved interaction model with Flame tokens/content rules;
- **WRAP** — Fluent-like primitive sits underneath a stronger Cereja-specific component;
- **CONDITIONAL** — define only when a real product/task needs it;
- **CEREJA-SPECIFIC** — Fluent does not express the editorial/knowledge job;
- **REJECT DEFAULT** — do not add merely because Fluent has it.

## Product surfaces Flame should be able to support

### Publication
- newsletter calling-card;
- archive;
- article/issue reading;
- subscribe/conversion;
- media/reference pages.

### Public lab
- Flame catalogue;
- experiments;
- provenance;
- component documentation;
- interactive examples.

### Research / knowledge app
- search;
- source/evidence browsing;
- thesis graph;
- filters;
- detail panes;
- comparison;
- saved views;
- agent/research runs.

### Editorial operations app
- packet status;
- evidence review;
- approvals;
- comments/feedback;
- form-based configuration;
- run history.

A component belongs in Flame because one of these product families needs it — not because a generic DS checklist says it should exist.

## Coverage matrix

Legend:

- **Current** — present in some form today;
- **Partial** — visual/example exists but no full component contract;
- **Missing** — no Flame contract yet.

| Capability / Fluent reference | Current Flame | Decision | Priority | Notes |
|---|---|---|---|---|
| Text | Partial | ADAPT | P0 | semantic roles + type tokens; connect to approved typography system |
| Link | Partial | ADAPT | P0 | inline/nav/external/source variants; focus + visited policy |
| Button | Partial | ADAPT | P0 | action semantics only; navigation uses Link/ActionLink styling; primary/secondary/subtle/icon; full state matrix |
| Icon | Partial | ADAPT | P0 | semantic icons, brand icon boundary, accessible-name contract |
| Image | Partial | ADAPT | P0 | content/decorative/evidence/conceptual + provenance |
| Divider | Partial | ADAPT | P0 | editorial rhythm vs UI grouping |
| Badge | Missing | ADAPT | P1 | small status/description indicator; do not use as generic decorative label |
| Tag | Partial | ADAPT | P0 | topic/status/selection must not collapse into one pill style |
| Surface / container | Partial | FLAME PRIMITIVE | P0 | not a Fluent React catalogue component; quiet/actionable/elevated/editorial; prevent card-everything |
| Field | Missing | ADOPT/ADAPT | P1 | standard label/help/error relationship |
| Label | Missing | ADOPT | P1 | form semantics |
| Input | Missing | ADAPT | P1 | text/search/filter settings |
| Textarea | Missing | ADAPT | P1 | notes, editorial input, prompts with clear AI boundary |
| Checkbox | Missing | ADAPT | P1 | multi-select/preferences |
| Radio group | Missing | ADAPT | P1 | short exclusive sets |
| Switch | Missing | ADAPT | P1 | immediate binary settings only |
| Select | Missing | ADAPT | P1 | native/simple choices |
| Dropdown | Missing | ADAPT | P1 | choice menus |
| Combobox | Missing | ADAPT | P1 | searchable/creatable option sets |
| Searchbox | Missing | ADAPT | P1 | core for archive/research surfaces |
| Accordion | Native-only | ADAPT | P1 | disclosure, not hierarchy navigation |
| Tabs / Tablist | Missing | ADAPT | P1 | related peer views; not site nav |
| Breadcrumb | Missing | ADAPT | P1 | research/docs hierarchy when depth exists |
| Nav | Partial | ADAPT | P1 | primary app/site navigation; distinct from Menu and Tabs |
| Menu | Missing | ADAPT | P1 | contextual actions/navigation |
| Tooltip | Missing | ADOPT | P1 | supplemental info only; never essential instruction |
| Dialog | Missing | ADAPT | P1 | confirmation/focused task; strong focus management |
| Drawer | Missing | ADAPT | P1 | filters/detail/secondary workspaces |
| Popover | Missing | ADAPT | P1 | local supplemental interaction |
| Toast | Missing | ADAPT | P1 | transient result/status; must not hide critical errors |
| Message bar / persistent message state | Missing | ADAPT | P1 | maps to Fluent Message bar; warning/error/info/success must remain persistent when action is required |
| Spinner | Missing | ADAPT | P1 | indeterminate processing |
| Skeleton | Missing | ADAPT | P1 | page/content loading without fake final content |
| Progress | Missing | ADAPT | P1 | long agent/import/research operations |
| List | Missing | ADAPT | P1 | simple repeated content/action rows |
| Table | Missing | FLAME CAPABILITY / CONDITIONAL | P2 | comparable rows/columns; not claimed as an entry in the current Fluent React overview baseline |
| Data grid | Missing | FLAME CAPABILITY / CONDITIONAL | P2 | interactive data tasks only; not claimed as an entry in the current Fluent React overview baseline |
| Tree | Missing | CONDITIONAL | P2 | thesis graph/folder hierarchy only when tree semantics fit |
| Toolbar | Missing | CONDITIONAL | P2 | dense editor/research actions |
| Card | Partial | WRAP | P2 | only for real object grouping; not default layout primitive |
| Carousel | Social-only | WRAP | P2 | web content browsing ≠ Visual Magazine sequence |
| Avatar | Missing | CONDITIONAL | P2 | people/collaboration context |
| Avatar group | Missing | CONDITIONAL | P3 | collaboration only |
| Persona | Missing | CONDITIONAL | P3 | people-centric enterprise surfaces |
| Info label | Missing | CONDITIONAL | P2 | dense settings/forms |
| Slider | Missing | CONDITIONAL | P3 | continuous bounded values only |
| Spin button | Missing | CONDITIONAL | P3 | numeric increment/decrement task only |
| Rating | Missing | REJECT DEFAULT | P3 | add only with a real rating task |
| Tag picker | Missing | CONDITIONAL | P2 | taxonomy/metadata authoring |
| Fluent Provider | Missing | IMPLEMENTATION ADAPTER | P2 | not a visible Flame component; only relevant if a Fluent React/Web Components adapter is actually used |
| People picker / other collaboration controls | Missing | OFF-CATALOG / CONDITIONAL | P3 | not part of the current Fluent React overview baseline; add only from a real collaboration workflow |

## Cereja-specific components

These should not be reduced to generic Fluent cards.

| Component | Product job | Base primitives |
|---|---|---|
| **IssueHero** | open an issue/story with editorial hierarchy | Text, Image, Link, metadata |
| **IssueCollection** | browse/archive issues without dashboard feel | List/Grid, Link, Tag |
| **EvidenceStack** | show claim/source/context/limits together | Surface, Link, metadata, disclosure |
| **SourceLine** | compact provenance near a claim/media item | Link, Text, Icon |
| **ResearchDesk** | research/workbench shell for evidence + notes + agents | Search, Tabs, Drawer, List/Table, status |
| **ThesisPanel** | thesis state, evidence strength, dissent/open questions | Surface, Badge/Tag, disclosure |
| **RunStatus** | show agent/tool/check lifecycle clearly | Progress, Alert, Badge, Timeline |
| **HumanGatePanel** | explicit approval/revise/escalate decision | Surface, Button, status, evidence |
| **VisualMagazine** | channel-native editorial sequence | Image, Text, SourceLine; not a generic carousel |
| **SignalSequence** | ordered editorial signals with different visual jobs | List/Carousel primitive only if behavior fits |
| **ExitQuestion** | close/open conversation without generic CTA pattern | Text, Link/Button |
| **MediaFigure** | image/video/art with caption, rights, alt/provenance | Image/Video, Text, SourceLine |
| **ContextManifestView** | inspect what entered/exited an agent run | List/Table, disclosure, status |
| **AgentReviewPanel** | findings, severity, evidence, human decision | Alert/Surface, List, Button |

## Missing DS capabilities beyond components

Component coverage alone will not make Flame mature.

Flame still needs explicit contracts for:

### State system
For every interactive component:

- default;
- hover;
- pressed;
- focus-visible;
- disabled;
- selected/checked;
- loading;
- error/success when applicable.

### Content design
For every component:

- label grammar;
- help/error copy;
- empty/loading text;
- truncation/wrapping;
- localization;
- user-generated/AI-generated content boundary.

### Layout
Define:

- page/container widths;
- editorial reading measure;
- application shell;
- responsive columns;
- side panels;
- dense data surfaces;
- breakpoints as behavior, not device labels.

### Theming
Current v0.2 is light-first.

Before declaring a general app DS, decide:

- whether dark mode is required;
- semantic color aliases independent of brand color names;
- high-contrast behavior;
- system/user theme preferences.

### Density
Publication and app/research work need different densities.

Define at least:

- editorial/comfortable;
- application/default;
- dense only if a real product needs it.

Do not let dense enterprise UI leak into the newsletter surface.

### Focus/navigation
Keyboard/focus contracts should be explicit for:

- dialogs;
- drawers;
- menus;
- comboboxes;
- tabs;
- trees;
- grids;
- research workspaces.

### AI/product states
Apps using agents need product patterns for:

- generating;
- waiting;
- partial result;
- source unavailable;
- tool denied;
- human approval required;
- retry;
- stale evidence;
- uncertain answer;
- agent failure.

These are product states, not chat-bubble decoration.

## Component contract — minimum completeness

A Flame component is not "defined" because HTML/CSS exists.

Each component needs:

1. purpose / use when;
2. do-not-use / alternative;
3. anatomy;
4. variants;
5. states;
6. interaction;
7. keyboard behavior;
8. accessibility semantics;
9. content rules;
10. responsive behavior;
11. motion;
12. tokens;
13. Fluent reference;
14. Cereja divergence;
15. anti-patterns;
16. implementation/API contract;
17. deterministic checks where possible;
18. visual/semantic human evals.

See [components/component-contract-template.md](components/component-contract-template.md).

## Recommended build sequence

### P0 — foundations that everything else needs
- Text
- Link
- Button
- Icon
- Image / MediaFigure
- Divider
- Tag
- Surface

### P1 — enough to build real apps
- Field + Label
- Input / Textarea
- Checkbox / Radio / Switch
- Select / Dropdown / Combobox
- Searchbox
- Accordion
- Tabs
- Menu
- Tooltip / Popover
- Dialog / Drawer
- Alert / Toast
- Spinner / Skeleton / Progress
- List

### P2 — knowledge/research/editorial operations
- Table
- DataGrid only if justified
- Breadcrumb
- Tag Picker
- Toolbar
- ResearchDesk
- EvidenceStack
- ThesisPanel
- RunStatus
- HumanGatePanel
- ContextManifestView
- AgentReviewPanel

### P3 — only after a real requirement
- Tree
- Slider
- SpinButton
- Avatar/Persona family
- Rating
- people pickers and other collaboration-specific controls

## Design-system agent gap discovered

The current Factory has:

- Flame UI Composer — executes/composes under Flame;
- Frontend Engineer — implements;
- Accessibility Auditor — independently audits;
- Experience Researcher — investigates user evidence.

There is no specialist whose primary job is **design-system architecture**:

- component coverage;
- primitive/compound boundaries;
- adopt/adapt/wrap/reject decisions;
- component API consistency;
- token/component coupling;
- maturity and deprecation.

This audit is evidence for a possible new on-demand role:

> **Design Systems Architect**

Do not add the role only from this document. Validate that the role remains distinct while defining the first P0 component family.

## Definition of success

Someone should be able to build:

1. the Cereja publication site;
2. the Flame catalogue;
3. a research/evidence application;
4. an editorial operations application;

without inventing new interaction patterns for every screen and without making every surface look like Fluent, Microsoft, a SaaS starter kit or an AI-generated dashboard.


## Official-catalogue reconciliation — 2026-10-04

The current Fluent 2 React overview includes Badge, Nav and Fluent Provider, which the first Flame audit had not classified explicitly. They are now represented above.

The first audit also mixed some Flame product capabilities with direct Fluent catalogue references. That is useful for planning, but the distinction now stays explicit: Surface/container is a Flame primitive concept; Table/DataGrid are product capabilities in this roadmap rather than claims about the current official React overview; people-picker/collaboration controls remain off-catalogue future needs unless a real workflow requires them.

This keeps Fluent as a solved-behavior reference without turning its catalogue into Flame's backlog by default.
