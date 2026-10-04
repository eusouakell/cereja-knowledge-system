from __future__ import annotations

import argparse
from pathlib import Path

from sensor_html import inspect_html_path


def validate_surface(report: dict) -> list[str]:
    errors: list[str] = []

    if not report["html_lang"]:
        errors.append("html element requires a non-empty lang attribute")
    if report["main_count"] != 1:
        errors.append(f"expected exactly one main landmark, found {report['main_count']}")
    if 1 not in report["heading_levels"]:
        errors.append("surface requires at least one h1")
    if report["images_missing_alt"]:
        errors.append(f"{report['images_missing_alt']} image(s) missing alt attribute")
    if report["links_missing_href"]:
        errors.append(f"{report['links_missing_href']} link(s) missing href")
    if report["unnamed_links"]:
        errors.append(f"{report['unnamed_links']} link(s) have no accessible name")
    if report["unnamed_buttons"]:
        errors.append(f"{report['unnamed_buttons']} button(s) have no accessible name")
    if report["nonnative_click_handlers"]:
        tags = ", ".join(report["nonnative_click_handlers"])
        errors.append(f"non-native clickable element(s) detected: {tags}")
    if report.get("missing_linked_stylesheets"):
        missing = ", ".join(report["missing_linked_stylesheets"])
        errors.append(f"local stylesheet(s) not found: {missing}")
    if (report["links"] or report["buttons"]) and not report["has_focus_style"]:
        errors.append("interactive surface requires an explicit :focus or :focus-visible style")
    if report["uses_keyframes"] and not report["has_reduced_motion"]:
        errors.append("motion detected without prefers-reduced-motion: reduce treatment")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Run deterministic Flame HTML gates.")
    parser.add_argument("html", type=Path)
    args = parser.parse_args()

    report = inspect_html_path(args.html)
    errors = validate_surface(report)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: deterministic Flame HTML gates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
