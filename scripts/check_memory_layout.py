from __future__ import annotations

import argparse
from pathlib import Path


EXPECTED_DIRS = [
    "memory/drafts",
    "memory/reflections",
    "memory/relationships",
    "memory/preferences",
    "memory/open-questions",
    "memory/system",
]

CURATED_DIRS = [
    "memory/reflections",
    "memory/relationships",
    "memory/preferences",
    "memory/open-questions",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a layered memory layout.")
    parser.add_argument("workspace", help="Workspace root to inspect")
    args = parser.parse_args()

    root = Path(args.workspace).expanduser().resolve()
    print(f"Workspace: {root}")

    memory_md = root / "MEMORY.md"
    print(f"MEMORY.md: {'present' if memory_md.exists() else 'missing'}")

    missing = []
    for rel in EXPECTED_DIRS:
        path = root / rel
        if path.is_dir():
            print(f"[ok] {rel}")
        else:
            print(f"[missing] {rel}")
            missing.append(rel)

    if missing:
        print("\nSuggested next step:")
        print("- Create only the missing curated rooms you actually need.")
    else:
        print("\nLayout check passed.")

    print("\nCurated room contents:")
    for rel in CURATED_DIRS:
        path = root / rel
        if not path.is_dir():
            continue
        file_count = sum(1 for item in path.rglob("*") if item.is_file())
        if file_count == 0:
            print(f"[empty] {rel}")
        else:
            print(f"[files={file_count}] {rel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
