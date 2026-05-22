from __future__ import annotations

import argparse
import re
from pathlib import Path


SECTION_HEADERS = {
    "draft": "## Draft-only paths",
    "curated": "## Curated retrieval paths",
    "palace": "## Palace or wiki source paths",
}


def parse_registry(text: str) -> dict[str, list[str]]:
    current = None
    data = {"draft": [], "curated": [], "palace": []}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        matched = False
        for key, header in SECTION_HEADERS.items():
            if line == header:
                current = key
                matched = True
                break
        if line.startswith("## ") and not matched:
            current = None
        if matched or current is None:
            continue
        bullet = re.match(r"^-\s+`?(.+?)`?$", line)
        if bullet:
            value = bullet.group(1).strip()
            if value and value != "none declared" and value not in data[current]:
                data[current].append(value)
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Memory With Rooms registry file.")
    parser.add_argument("registry", help="Path to room-registry.md")
    args = parser.parse_args()

    registry_path = Path(args.registry).expanduser().resolve()
    text = registry_path.read_text(encoding="utf-8")
    data = parse_registry(text)

    draft = set(data["draft"])
    curated = set(data["curated"])
    palace = set(data["palace"])

    print(f"Registry: {registry_path}")
    print(f"Draft paths: {len(draft)}")
    print(f"Curated paths: {len(curated)}")
    print(f"Palace paths: {len(palace)}")

    overlap_dc = sorted(draft & curated)
    overlap_dp = sorted(draft & palace)

    if overlap_dc:
        print("\n[warning] Draft paths also marked as curated:")
        for item in overlap_dc:
            print(f"- {item}")

    if overlap_dp:
        print("\n[warning] Draft paths also marked as palace/wiki sources:")
        for item in overlap_dp:
            print(f"- {item}")

    if not overlap_dc and not overlap_dp:
        print("\nRegistry check passed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
