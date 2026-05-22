from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> None:
    print(f"> {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a basic smoke test for Memory With Rooms.")
    parser.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Skill root directory (defaults to the script's parent skill folder)",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    demo = root / "assets" / "demo-workspace"
    registry = demo / "memory" / "system" / "room-registry.md"

    run([sys.executable, str(root / "scripts" / "check_memory_layout.py"), str(demo)])
    run([sys.executable, str(root / "scripts" / "check_room_registry.py"), str(registry)])
    run([
        sys.executable,
        str(root / "scripts" / "build_registry.py"),
        "--workspace",
        str(demo),
        "--draft",
        "memory/drafts/",
        "--curated",
        "memory/reflections/",
        "--curated",
        "memory/relationships/",
        "--curated",
        "memory/preferences/",
        "--curated",
        "memory/open-questions/",
        "--palace",
        "memory/reflections/",
        "--palace",
        "memory/relationships/",
        "--palace",
        "memory/preferences/",
        "--palace",
        "memory/open-questions/",
        "--output",
        "memory/system/generated-room-registry.md",
    ])
    print("\nSmoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
