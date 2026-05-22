from __future__ import annotations

import argparse
from pathlib import Path


def normalize_paths(values: list[str]) -> list[str]:
    cleaned = []
    for value in values:
        item = value.strip()
        if item and item not in cleaned:
            cleaned.append(item)
    return cleaned


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a simple room registry markdown file.")
    parser.add_argument("--workspace", required=True, help="Workspace root")
    parser.add_argument("--draft", action="append", default=[], help="Draft-only path")
    parser.add_argument("--curated", action="append", default=[], help="Curated retrieval path")
    parser.add_argument("--palace", action="append", default=[], help="Path that may feed palace/wiki layers")
    parser.add_argument("--output", default="memory/system/room-registry.md", help="Output path relative to workspace")
    args = parser.parse_args()

    root = Path(args.workspace).expanduser().resolve()
    output_path = root / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)

    drafts = normalize_paths(args.draft)
    curated = normalize_paths(args.curated)
    palace = normalize_paths(args.palace)

    lines = [
        "# Room Registry",
        "",
        "## Draft-only paths",
    ]
    lines.extend([f"- `{item}`" for item in drafts] or ["- none declared"])
    lines.extend([
        "",
        "## Curated retrieval paths",
    ])
    lines.extend([f"- `{item}`" for item in curated] or ["- none declared"])
    lines.extend([
        "",
        "## Palace or wiki source paths",
    ])
    lines.extend([f"- `{item}`" for item in palace] or ["- none declared"])
    lines.extend([
        "",
        "## Notes",
        "- Draft-only paths should not be the default source for normal recall.",
        "- Curated paths should contain concise material worth finding later.",
        "- Palace/wiki layers should ingest curated paths before drafts.",
        "",
    ])

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote registry: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
