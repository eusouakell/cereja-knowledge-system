# Flame Button / Action control

Status: **pilot component contract**.

Owner: Flame.

This is the first P0 component contract used to calibrate how Fluent behavior becomes a Flame component without importing Microsoft visual identity.

## Purpose

Trigger a discrete action.

Examples:
- submit a form;
- approve or revise;
- start a bounded operation;
- confirm or cancel a dialog;
- retry a failed task.

Navigation is not a button job.

A link may share the same visual treatment, but if activation changes location rather than executes an action, the semantic component is Link / ActionLink.

## Use when

- the user can take a discrete action now;
- state changes directly as a result of activation;
- the action has a clear verb and outcome.

## Do not use when

- navigating to another page or URL: use Link / ActionLink;
- choosing a persistent binary setting: use Switch;
- selecting one item from a short exclusive set: use Radio Group;
- exposing several contextual commands: use Menu;
- the entire surface is the navigation target: use an appropriate link pattern.

## Fluent reference

Fluent component: Button  
Reference: https://fluent2.microsoft.design/components/web/react/core/button/usage  
Decision: **ADAPT**

Behavior retained from Fluent:
- action vs navigation distinction;
- primary/secondary action hierarchy;
- toggle behavior only when semantically appropriate;
- disabled-state explanation when needed;
- action-oriented labels;
- one dominant primary action in a decision area.

## Flame divergence

Flame supplies:
- cherry action color;
- 6px control radius;
- editorial spacing/rhythm;
- restrained shadow/motion;
- copy appropriate to Cereja and product context;
- no Microsoft/Fluent visual mimicry.

## Anatomy

1. semantic button element;
2. text label;
3. optional leading or trailing semantic icon;
4. optional progress/loading indicator;
5. optional accessible description when context is not fully visible.

## Variants

| Variant | Use |
|---|---|
| primary | single dominant action in a decision area |
| secondary | valid alternative with lower visual weight |
| subtle | lower-priority local action |
| transparent/text | very low visual weight where button semantics are still required |
| icon | compact action only when icon meaning is established and accessible name is explicit |
| danger | destructive/irreversible action; never encoded by color alone |

Split/menu/compound/toggle behaviors are not automatically part of Flame Button v0.1. Add them only when a real product task requires them.

## States

Required:
- default;
- hover;
- pressed;
- focus-visible;
- disabled;
- loading where asynchronous action exists.

Conditional:
- selected/checked only for explicit toggle-button behavior;
- success/error normally belongs to the surrounding product state, not a permanently recolored button.

## Content rules

Labels should:
- start with a concrete action verb;
- include the object when the verb alone is ambiguous;
- use sentence case;
- avoid end punctuation in ordinary labels;
- describe the next action, not a vague benefit.

Prefer:
- Salvar alterações
- Aprovar edição
- Tentar novamente
- Excluir fonte

Avoid:
- Continuar when the actual action can be named;
- OK for dismissing an error;
- promotional CTA language inside operational apps.

Cancel and Close are different:
- Cancel abandons a task or change;
- Close dismisses a surface without implying rollback.

## Interaction

Pointer/touch:
- one activation triggers one action;
- repeated activation must not duplicate a non-idempotent action;
- destructive actions follow the product confirmation/undo contract.

Keyboard:
- native button activation semantics;
- focus order follows DOM/task order;
- Enter/Space behavior stays native unless a specialized pattern documents otherwise.

Focus:
- visible focus ring must not be removed;
- opening a new surface hands focus according to that surface contract.

## Accessibility

Use native button semantics for actions whenever possible.

Accessible name:
- visible label preferred;
- icon-only controls require explicit accessible name;
- state must not depend on color or icon alone.

Contrast target:
- button text at least 4.5:1 against its background;
- meaningful icons at least 3:1 against their background.

Target size:
- Flame product target remains approximately 48px minimum interactive height where layout permits.

Disabled:
- disabled state must not be the only explanation of why an action is unavailable;
- provide nearby help/status or tooltip when the reason is not obvious.

Automated checks do not prove full accessibility.

## Responsive behavior

- labels wrap only when the product context can tolerate multi-line controls;
- action groups may stack on narrow containers;
- primary action remains perceptually dominant without forcing visual order to diverge from DOM order;
- do not shrink operational labels until meaning is lost.

## Motion

Allowed:
- fast state feedback;
- subtle shadow/transform only if it communicates interaction.

Current Flame reference:
- motion-fast: 160ms
- ease-standard: cubic-bezier(.2,.7,.2,1)

Do not:
- animate every button entrance;
- use bounce/spring as generic delight;
- require motion to understand state.

Reduced motion:
- action remains fully understandable with transitions removed.

## Tokens

Current pilot mapping:
- primary background: color-action;
- primary foreground: white;
- focus: color-focus;
- radius: radius-control;
- motion: motion-fast + ease-standard.

Secondary boundary currently reuses color-action in the prototype because the previous neutral border was too low-contrast to identify the control boundary reliably.

This mapping is a pilot, not permission to introduce raw values in product code.

## Semantic implementation direction

Button:
- variant: primary | secondary | subtle | transparent | danger
- size: default | compact
- loading
- disabled
- leadingIcon
- trailingIcon
- onAction

Navigation counterpart:
- ActionLink
- appearance: primary | secondary | subtle
- href

Visual recipes may be shared internally. Semantics may not be collapsed.

## Deterministic checks

Where code is available:
- interactive action uses native button semantics unless an exception is documented;
- navigation variant has a valid href;
- icon-only control has an accessible name;
- disabled/loading state does not leave duplicate action enabled;
- focus-visible treatment is present;
- no approval-looking button implies authority not granted by the product/control plane.

## Human evals

- action hierarchy is clear;
- number of prominent actions is justified;
- label is specific to the task;
- visual treatment feels Flame rather than Fluent/Microsoft default;
- destructive action weight matches consequence;
- no generic SaaS CTA pattern leaks into editorial surfaces.

## Anti-patterns

- styling every link as a button;
- one primary button per card in a repeated grid;
- multiple equally loud primary actions;
- generic "Gerar com IA" button without visible agent/run state;
- icon-only actions whose meaning depends on familiarity;
- disabled control with no explanation;
- using a button to navigate because the design wanted a filled rectangle;
- cherry fill used so often that it stops expressing priority.

## Examples

Good:
- Aprovar edição after evidence/review is visible;
- Tentar novamente after a failed bounded run;
- Assinar a Cereja rendered semantically as an ActionLink when it navigates to Substack.

Bad:
- Saiba mais repeated under every card;
- Continuar when the next state is actually Publicar;
- a fake button built from div + click handler;
- a primary cherry button for every minor action.

## Provenance

- Fluent Button behavior/content/accessibility reference reviewed 2026-10-04;
- Flame v0.2 prototype provides current token/visual evidence;
- accessibility Issue #16 and subsequent fixes inform focus/control-boundary rules;
- canonical promotion requires Kell approval after at least one real product/app implementation.
