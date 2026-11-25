#!/usr/bin/env python3
"""Scaffold a blank Python problem or redo file using the 6-step problem loop template.

Examples:
    python scripts/new_problem.py 01 "Two Sum" --difficulty Easy --url "https://leetcode.com/problems/two-sum/"
    python scripts/new_problem.py redo "Two Sum" --pattern "Arrays & Hashing" --difficulty Easy
    python scripts/new_problem.py unseen "Majority Element" --difficulty Easy
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "templates" / "solution_template.py"

FOLDER_MAP = {
    "00": ("00-pre-week-python", "Pre-Week Python"),
    "01": ("01-arrays-and-hashing", "Arrays & Hashing"),
    "02": ("02-two-pointers", "Two Pointers"),
    "03": ("03-stack", "Stack"),
    "04": ("04-binary-search", "Binary Search"),
    "05": ("05-sliding-window", "Sliding Window"),
    "06": ("06-linked-list", "Linked List"),
    "07": ("07-trees", "Trees"),
    "08": ("08-heap-and-priority-queue", "Heap / Priority Queue"),
    "09": ("09-tries", "Tries"),
    "10": ("10-backtracking", "Backtracking"),
    "11": ("11-graphs", "Graphs"),
    "12": ("12-advanced-graphs", "Advanced Graphs"),
    "13": ("13-1d-dynamic-programming", "1-D Dynamic Programming"),
    "14": ("14-2d-dynamic-programming", "2-D Dynamic Programming"),
    "15": ("15-greedy", "Greedy"),
    "16": ("16-intervals", "Intervals"),
    "17": ("17-bit-manipulation", "Bit Manipulation"),
    "18": ("18-math-and-matrix", "Math & Matrix"),
    "scratch": ("from-scratch", "From Scratch"),
    "redo": ("redos", "Spaced Redo"),
    "unseen": ("timed-practice/unseen-transfer", "Unseen Transfer"),
    "checkpoint": ("timed-practice/checkpoints", "Checkpoint"),
    "oa": ("timed-practice/online-assessments", "Online Assessment"),
    "sim": ("timed-practice/simulations", "Full Simulation"),
}


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", name.strip().lower()).strip("_")
    return slug or "problem"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new DSA problem file from template.")
    parser.add_argument(
        "target",
        help="Folder key (00..18, scratch, redo, unseen, checkpoint, oa, sim) or exact folder name.",
    )
    parser.add_argument("problem", help="Problem title, e.g. 'Two Sum'")
    parser.add_argument("--difficulty", "-d", default="Medium", choices=["Easy", "Medium", "Hard"])
    parser.add_argument("--pattern", "-p", default="", help="Override pattern name in header")
    parser.add_argument("--url", "-u", default="", help="LeetCode or NeetCode problem URL")
    args = parser.parse_args()

    key = args.target.lower()
    if key in FOLDER_MAP:
        rel_dir, default_pattern = FOLDER_MAP[key]
    else:
        matched = [v for v in FOLDER_MAP.values() if v[0] == args.target]
        if matched:
            rel_dir, default_pattern = matched[0]
        else:
            valid = ", ".join(sorted(FOLDER_MAP.keys()))
            raise SystemExit(f"Unknown target '{args.target}'. Valid targets: {valid}")

    today = dt.date.today().isoformat()
    slug = slugify(args.problem)
    filename = f"{today}_{slug}.py" if key in {"redo", "unseen", "checkpoint", "oa", "sim"} else f"{slug}.py"
    dest_dir = ROOT / rel_dir
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / filename

    if dest_path.exists():
        raise SystemExit(f"File already exists: {dest_path.relative_to(ROOT)}")

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    content = template.format(
        problem=args.problem,
        url=args.url or "https://leetcode.com/problemset/",
        pattern=args.pattern or default_pattern,
        difficulty=args.difficulty,
        date=today,
    )
    dest_path.write_text(content, encoding="utf-8")
    print(f"Created {dest_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
