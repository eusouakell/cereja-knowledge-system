import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISUAL = ROOT / "brand" / "flame" / "visual-delivery"
sys.path.insert(0, str(VISUAL))

from check_html import validate_surface
from sensor_html import inspect_html, inspect_html_path


PASSING = """<!doctype html>
<html lang="pt-BR">
<head>
  <title>Flame specimen</title>
  <style>
    :root { --color-action-primary: #BE1035; }
    a:focus-visible, button:focus-visible { outline: 3px solid currentColor; }
    @keyframes enter { from { opacity: 0; } to { opacity: 1; } }
    .hero { animation: enter 160ms ease-out both; }
    @media (prefers-reduced-motion: reduce) {
      .hero { animation: none; }
    }
  </style>
</head>
<body>
  <header><nav><a href="#content">Pular para conteúdo</a></nav></header>
  <main id="content">
    <h1 class="hero">Cereja</h1>
    <img src="cover.jpg" alt="Ilustração editorial abstrata">
    <button type="button" aria-label="Assinar"></button>
  </main>
</body>
</html>
"""


LINKED = """<!doctype html>
<html lang="pt-BR">
<head>
  <title>Flame linked specimen</title>
  <link rel="stylesheet" href="tokens.css">
</head>
<body>
  <main id="content">
    <h1 class="hero">Cereja</h1>
    <a href="#more">Continuar</a>
  </main>
</body>
</html>
"""


LINKED_CSS = """
a:focus-visible { outline: 3px solid currentColor; }
@keyframes enter { from { opacity: 0; } to { opacity: 1; } }
.hero { animation: enter 160ms ease-out both; }
@media (prefers-reduced-motion: reduce) {
  .hero { animation: none; }
}
"""


class FlameVisualGateTests(unittest.TestCase):
    def test_passing_surface_clears_deterministic_gates(self):
        self.assertEqual(validate_surface(inspect_html(PASSING)), [])

    def test_missing_alt_fails(self):
        broken = PASSING.replace('alt="Ilustração editorial abstrata"', "")
        errors = validate_surface(inspect_html(broken))
        self.assertTrue(any("missing alt" in error for error in errors))

    def test_motion_without_reduced_motion_fails(self):
        broken = PASSING.replace(
            '@media (prefers-reduced-motion: reduce) {\n      .hero { animation: none; }\n    }',
            "",
        )
        errors = validate_surface(inspect_html(broken))
        self.assertTrue(any("prefers-reduced-motion" in error for error in errors))

    def test_visual_sensor_keeps_heading_jump_as_observation(self):
        observed = PASSING.replace("</h1>", "</h1><h3>Referências</h3>")
        report = inspect_html(observed)
        self.assertEqual(report["heading_jumps"], [{"from": 1, "to": 3}])
        self.assertEqual(validate_surface(report), [])

    def test_local_linked_stylesheet_contributes_to_real_surface_audit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            html = root / "site.html"
            css = root / "tokens.css"
            html.write_text(LINKED, encoding="utf-8")
            css.write_text(LINKED_CSS, encoding="utf-8")

            report = inspect_html_path(html)

            self.assertEqual(report["linked_stylesheets"], ["tokens.css"])
            self.assertEqual(report["resolved_linked_stylesheets"], ["tokens.css"])
            self.assertEqual(report["missing_linked_stylesheets"], [])
            self.assertTrue(report["has_focus_style"])
            self.assertTrue(report["uses_keyframes"])
            self.assertTrue(report["has_reduced_motion"])
            self.assertEqual(validate_surface(report), [])

    def test_root_relative_local_stylesheet_resolves_from_repository_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            assets = root / "assets"
            pages = root / "pages"
            assets.mkdir()
            pages.mkdir()
            html = pages / "site.html"
            css = assets / "site.css"
            html.write_text(
                LINKED.replace("tokens.css", "/assets/site.css"),
                encoding="utf-8",
            )
            css.write_text(LINKED_CSS, encoding="utf-8")

            report = inspect_html_path(html, repository_root=root)

            self.assertEqual(
                report["resolved_linked_stylesheets"],
                ["assets/site.css"],
            )
            self.assertEqual(report["skipped_external_stylesheets"], [])
            self.assertEqual(validate_surface(report), [])

    def test_missing_local_stylesheet_fails_explicitly(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            html = root / "site.html"
            html.write_text(
                LINKED.replace("tokens.css", "missing.css"),
                encoding="utf-8",
            )

            report = inspect_html_path(html)
            errors = validate_surface(report)

            self.assertEqual(report["missing_linked_stylesheets"], ["missing.css"])
            self.assertTrue(any("local stylesheet(s) not found" in error for error in errors))

    def test_remote_stylesheet_is_observed_but_not_fetched(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            html = root / "site.html"
            html.write_text(
                LINKED.replace("tokens.css", "https://example.com/site.css"),
                encoding="utf-8",
            )

            report = inspect_html_path(html)

            self.assertEqual(
                report["skipped_external_stylesheets"],
                ["https://example.com/site.css"],
            )


if __name__ == "__main__":
    unittest.main()
