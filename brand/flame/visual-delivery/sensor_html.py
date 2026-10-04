from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class SurfaceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = ""
        self.main_count = 0
        self.headings: list[int] = []
        self.images: list[dict[str, str | None]] = []
        self.links: list[dict[str, object]] = []
        self.buttons: list[dict[str, object]] = []
        self.stylesheets: list[str] = []
        self.inline_style_attrs = 0
        self.nonnative_clickables: list[str] = []
        self.landmarks: dict[str, int] = {}
        self._interactive_stack: list[dict[str, object]] = []

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrs_list)
        if tag == "html":
            self.html_lang = (attrs.get("lang") or "").strip()
        if tag == "main":
            self.main_count += 1
        if tag in {"main", "nav", "header", "footer", "aside"}:
            self.landmarks[tag] = self.landmarks.get(tag, 0) + 1
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))
        if "style" in attrs:
            self.inline_style_attrs += 1
        if tag == "link":
            rel = (attrs.get("rel") or "").lower().split()
            href = (attrs.get("href") or "").strip()
            if "stylesheet" in rel and href:
                self.stylesheets.append(href)
        if tag == "img":
            self.images.append({"alt": attrs.get("alt"), "src": attrs.get("src")})
            if self._interactive_stack and attrs.get("alt"):
                self._interactive_stack[-1]["text"] += " " + (attrs.get("alt") or "")
        if tag in {"a", "button"}:
            node = {
                "tag": tag,
                "href": attrs.get("href"),
                "aria_label": attrs.get("aria-label"),
                "aria_labelledby": attrs.get("aria-labelledby"),
                "text": "",
            }
            self._interactive_stack.append(node)
        if "onclick" in attrs and tag not in {"a", "button", "input", "select", "textarea"}:
            self.nonnative_clickables.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"a", "button"} and self._interactive_stack:
            node = self._interactive_stack.pop()
            node["text"] = str(node["text"]).strip()
            if tag == "a":
                self.links.append(node)
            else:
                self.buttons.append(node)

    def handle_data(self, data: str) -> None:
        if self._interactive_stack:
            self._interactive_stack[-1]["text"] += data


def _repo_root(path: Path) -> Path:
    resolved = path.resolve()
    for parent in (resolved.parent, *resolved.parents):
        if (parent / ".git").exists():
            return parent
    return resolved.parent


def _local_stylesheet_path(html_path: Path, href: str, repo_root: Path) -> Path | None:
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc or href.startswith("//") or href.startswith("data:"):
        return None

    relative = unquote(parsed.path).strip()
    if not relative:
        return None

    candidate = (html_path.parent / relative).resolve()
    try:
        candidate.relative_to(repo_root.resolve())
    except ValueError:
        return None
    return candidate


def inspect_html(text: str, linked_css: str = "") -> dict:
    parser = SurfaceParser()
    parser.feed(text)

    inline_css = " ".join(
        re.findall(r"<style[^>]*>(.*?)</style>", text, re.DOTALL | re.IGNORECASE)
    )
    css = f"{inline_css}\n{linked_css}"

    heading_jumps = [
        {"from": previous, "to": current}
        for previous, current in zip(parser.headings, parser.headings[1:])
        if current - previous > 1
    ]

    return {
        "html_lang": parser.html_lang,
        "main_count": parser.main_count,
        "heading_levels": parser.headings,
        "heading_jumps": heading_jumps,
        "landmarks": parser.landmarks,
        "images": len(parser.images),
        "links": len(parser.links),
        "buttons": len(parser.buttons),
        "linked_stylesheets": parser.stylesheets,
        "resolved_linked_stylesheets": [],
        "missing_linked_stylesheets": [],
        "skipped_external_stylesheets": [],
        "inline_style_attributes": parser.inline_style_attrs,
        "raw_hex_literals": len(re.findall(r"#[0-9a-fA-F]{3,8}\b", css)),
        "uses_keyframes": bool(re.search(r"@keyframes\b|\banimation\s*:", css, re.IGNORECASE)),
        "has_reduced_motion": bool(
            re.search(r"prefers-reduced-motion\s*:\s*reduce", css, re.IGNORECASE)
        ),
        "has_focus_style": bool(re.search(r":focus(?:-visible)?\b", css, re.IGNORECASE)),
        "images_missing_alt": sum(1 for image in parser.images if image["alt"] is None),
        "links_missing_href": sum(1 for link in parser.links if not link["href"]),
        "unnamed_links": sum(
            1
            for link in parser.links
            if not link["text"] and not link["aria_label"] and not link["aria_labelledby"]
        ),
        "unnamed_buttons": sum(
            1
            for button in parser.buttons
            if not button["text"] and not button["aria_label"] and not button["aria_labelledby"]
        ),
        "nonnative_click_handlers": parser.nonnative_clickables,
    }


def inspect_html_path(path: Path, repository_root: Path | None = None) -> dict:
    path = path.resolve()
    root = (repository_root or _repo_root(path)).resolve()
    text = path.read_text(encoding="utf-8")

    parser = SurfaceParser()
    parser.feed(text)

    css_parts: list[str] = []
    resolved: list[str] = []
    missing: list[str] = []
    skipped_external: list[str] = []

    for href in parser.stylesheets:
        target = _local_stylesheet_path(path, href, root)
        if target is None:
            skipped_external.append(href)
            continue
        if not target.is_file():
            missing.append(href)
            continue

        css_parts.append(target.read_text(encoding="utf-8"))
        resolved.append(str(target.relative_to(root)))

    report = inspect_html(text, "\n".join(css_parts))
    report["resolved_linked_stylesheets"] = resolved
    report["missing_linked_stylesheets"] = missing
    report["skipped_external_stylesheets"] = skipped_external
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Observe a Flame HTML artifact and local linked stylesheets."
    )
    parser.add_argument("html", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report = inspect_html_path(args.html)
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
