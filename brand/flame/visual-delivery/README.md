# Flame visual delivery

Status: **experimental controls**.

This folder separates three questions that screenshot-to-code systems often collapse:

1. **Does it look close?** → sensor.
2. **Does it preserve deterministic semantic/accessibility invariants?** → check.
3. **Does it solve the right editorial/design problem in a Cereja way?** → human Flame gate.

## Files

- `reference-evaluation.md` — external pattern review and adoption boundary;
- `sensor_html.py` — observations from HTML plus local linked stylesheets;
- `check_html.py` — deterministic semantics/accessibility gates;
- `specimen.html` — minimal CI specimen, not a canonical template.

## CSS coverage

The sensor resolves relative/local `<link rel="stylesheet">` files inside the checked-out repository.

It does **not** fetch remote stylesheets. Remote CSS is reported in `skipped_external_stylesheets` rather than silently treated as inspected.

Missing local stylesheets are a deterministic gate failure because the tool cannot truthfully evaluate focus/motion CSS that should have been available in the repository.

## Run

```bash
python brand/flame/visual-delivery/sensor_html.py \
  brand/flame/visual-delivery/specimen.html

python brand/flame/visual-delivery/check_html.py \
  brand/flame/visual-delivery/specimen.html

python brand/flame/visual-delivery/check_html.py \
  brand/flame/prototype/index.html

python brand/flame/visual-delivery/check_html.py \
  brand/flame/prototype/site.html

python -m unittest discover -s tests -v
```

## CI scope

`Flame Visual Gates` runs when either:

- visual-delivery tooling/tests change; or
- the source-controlled Flame prototype changes.

The prototype therefore exercises the deterministic gate against a real linked-CSS surface rather than only a self-contained specimen.

## Principle

**Visual fidelity can ask for another iteration. It cannot waive semantics or accessibility.**
