from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


REQ_START = "[REQUIREMENT]"


def parse_requirements(text: str) -> list[dict]:
    """Parse only the small field subset used by this pilot.

    StrictDoc remains the authoritative syntax validator. This parser exists
    solely to derive observability metrics from the already validated source.
    """
    requirements: list[dict] = []
    chunks = text.split(REQ_START)[1:]
    for chunk in chunks:
        uid_match = re.search(r"^UID:\s*(.+)$", chunk, re.MULTILINE)
        tags_match = re.search(r"^TAGS:\s*(.+)$", chunk, re.MULTILINE)
        if not uid_match:
            continue
        parents = re.findall(
            r"- TYPE:\s*Parent\s*\n\s*VALUE:\s*(.+)$",
            chunk,
            re.MULTILINE,
        )
        requirements.append(
            {
                "uid": uid_match.group(1).strip(),
                "tags": [tag.strip() for tag in tags_match.group(1).split(",")]
                if tags_match
                else [],
                "parents": [parent.strip() for parent in parents],
            }
        )
    return requirements


def snapshot(requirements: list[dict]) -> dict:
    by_level = Counter(
        tag
        for requirement in requirements
        for tag in requirement["tags"]
        if re.fullmatch(r"L[0-9]+", tag)
    )
    relation_count = sum(len(requirement["parents"]) for requirement in requirements)
    roots = [r["uid"] for r in requirements if not r["parents"]]
    multi_parent = [r["uid"] for r in requirements if len(r["parents"]) > 1]

    return {
        "requirements": len(requirements),
        "relations": relation_count,
        "by_level": dict(sorted(by_level.items())),
        "roots": roots,
        "multi_parent_requirements": multi_parent,
        "relation_density": round(relation_count / len(requirements), 3)
        if requirements
        else 0.0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Observe Flame traceability graph.")
    parser.add_argument("document", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report = snapshot(parse_requirements(args.document.read_text(encoding="utf-8")))
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    print(rendered)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
