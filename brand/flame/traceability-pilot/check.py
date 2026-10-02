from __future__ import annotations

import argparse
from pathlib import Path

from sensor import parse_requirements


def validate_graph(requirements: list[dict]) -> list[str]:
    errors: list[str] = []
    by_uid = {requirement["uid"]: requirement for requirement in requirements}

    if len(by_uid) != len(requirements):
        errors.append("duplicate UID detected by pilot check")

    for requirement in requirements:
        uid = requirement["uid"]
        levels = [tag for tag in requirement["tags"] if tag.startswith("L")]
        level = levels[0] if levels else None

        if level != "L0" and not requirement["parents"]:
            errors.append(f"{uid}: non-L0 requirement has no Parent relation")

        for parent in requirement["parents"]:
            if parent not in by_uid:
                errors.append(f"{uid}: unresolved parent {parent}")

    def reaches_l0(uid: str, seen: set[str] | None = None) -> bool:
        seen = set() if seen is None else seen
        if uid in seen:
            return False
        seen.add(uid)

        requirement = by_uid.get(uid)
        if requirement is None:
            return False
        if "L0" in requirement["tags"]:
            return True
        return any(reaches_l0(parent, seen.copy()) for parent in requirement["parents"])

    for requirement in requirements:
        if "L0" not in requirement["tags"] and not reaches_l0(requirement["uid"]):
            errors.append(f"{requirement['uid']}: no trace path reaches an L0 requirement")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Flame traceability graph.")
    parser.add_argument("document", type=Path)
    args = parser.parse_args()

    requirements = parse_requirements(args.document.read_text(encoding="utf-8"))
    errors = validate_graph(requirements)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print(f"PASS: {len(requirements)} requirements have valid pilot trace paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
