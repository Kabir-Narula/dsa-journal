#!/usr/bin/env python3
"""Spaced-repetition (1-3-7-21) tracker CLI for DSA Journal.

Commands:
    python scripts/tracker_cli.py due
    python scripts/tracker_cli.py stats
    python scripts/tracker_cli.py log --problem "Two Sum" --pattern "Arrays & Hashing" \
        --difficulty Easy --minutes 18 --hint 0 --result Clean --mistake "None"
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parent.parent
LOG_PATH = ROOT / "tracker" / "problem_log.csv"

FIELDNAMES = [
    "Date",
    "Problem",
    "Pattern",
    "Difficulty",
    "Minutes",
    "Hint_Level",
    "Result",
    "Mistake",
    "Redo_Stage",
    "Next_Redo",
]

# 1-3-7-21 spaced repetition intervals (in days)
REDO_INTERVALS = [1, 3, 7, 21]


def load_rows() -> list[dict[str, str]]:
    if not LOG_PATH.exists():
        return []
    with LOG_PATH.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def save_rows(rows: list[dict[str, str]]) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def compute_next_redo(
    attempt_date: dt.date,
    minutes: int,
    hint: int,
    result: str,
    prev_stage: int,
) -> tuple[str, str]:
    """Apply roadmap 1-3-7-21 rules.

    - Failed, hint >= 2, or minutes > 35 resets the clock to Day 1 (stage 1).
    - Redo attempt must be Clean and <= 20 min to advance; otherwise reset to Day 1.
    - Clean first attempt (<= 35 min, hint <= 1) schedules a 7-day verification redo
      (stage 3) or marks Done once stage 4 (day 21) is passed.
    """
    is_redo = prev_stage > 0
    if result == "Failed" or hint >= 2 or (not is_redo and minutes > 35) or (is_redo and (result != "Clean" or minutes > 20)):
        next_date = attempt_date + dt.timedelta(days=REDO_INTERVALS[0])
        return "1", next_date.isoformat()

    if not is_redo:
        # Clean initial solve -> schedule 7-day check to confirm long-term recall
        next_date = attempt_date + dt.timedelta(days=7)
        return "3", next_date.isoformat()

    next_stage = prev_stage + 1
    if next_stage > len(REDO_INTERVALS):
        return "Done", ""
    next_date = attempt_date + dt.timedelta(days=REDO_INTERVALS[next_stage - 1])
    return str(next_stage), next_date.isoformat()


def cmd_log(args: argparse.Namespace) -> None:
    rows = load_rows()
    attempt_date = dt.date.fromisoformat(args.date) if args.date else dt.date.today()

    # Determine previous redo stage for this problem (latest row)
    prev_stage = 0
    for row in reversed(rows):
        if row["Problem"].strip().lower() == args.problem.strip().lower():
            stage_str = row.get("Redo_Stage", "").strip()
            if stage_str.isdigit():
                prev_stage = int(stage_str)
            elif stage_str.lower() == "done":
                prev_stage = len(REDO_INTERVALS)
            break

    stage, next_redo = compute_next_redo(
        attempt_date=attempt_date,
        minutes=args.minutes,
        hint=args.hint,
        result=args.result,
        prev_stage=prev_stage,
    )

    new_row = {
        "Date": attempt_date.isoformat(),
        "Problem": args.problem.strip(),
        "Pattern": args.pattern.strip(),
        "Difficulty": args.difficulty,
        "Minutes": str(args.minutes),
        "Hint_Level": str(args.hint),
        "Result": args.result,
        "Mistake": args.mistake.strip(),
        "Redo_Stage": stage,
        "Next_Redo": next_redo,
    }
    rows.append(new_row)
    save_rows(rows)

    print(f"Logged: {new_row['Problem']} ({new_row['Difficulty']}) -> {new_row['Result']} in {new_row['Minutes']}m")
    if next_redo:
        print(f"Next redo (stage {stage}/4): {next_redo}")
    else:
        print("Status: Mastered (Done!)")


def latest_by_problem(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    latest: dict[str, dict[str, str]] = {}
    for row in rows:
        key = row["Problem"].strip().lower()
        if key:
            latest[key] = row
    return latest


def cmd_due(args: argparse.Namespace) -> None:
    rows = load_rows()
    today = dt.date.fromisoformat(args.as_of) if args.as_of else dt.date.today()
    latest = latest_by_problem(rows)

    due_items: list[tuple[dt.date, dict[str, str]]] = []
    upcoming: list[tuple[dt.date, dict[str, str]]] = []

    for row in latest.values():
        nr = row.get("Next_Redo", "").strip()
        if not nr:
            continue
        try:
            due_date = dt.date.fromisoformat(nr)
        except ValueError:
            continue
        if due_date <= today:
            due_items.append((due_date, row))
        else:
            upcoming.append((due_date, row))

    due_items.sort(key=lambda x: x[0])
    upcoming.sort(key=lambda x: x[0])

    print(f"=== Redo Queue as of {today.isoformat()} ===")
    if not due_items:
        print("No redos due today. Great job staying caught up!")
    else:
        for d, row in due_items:
            overdue = (today - d).days
            tag = f"OVERDUE {overdue}d" if overdue > 0 else "DUE TODAY"
            print(
                f"  [{tag:10}] {row['Problem']} ({row['Pattern']}, {row['Difficulty']}) "
                f"| Stage {row['Redo_Stage']}/4 | Last mistake: {row['Mistake'] or '-'}"
            )

    if upcoming:
        print("\nNext up:")
        for d, row in upcoming[:5]:
            print(f"  {d.isoformat()}  {row['Problem']} ({row['Pattern']}) [Stage {row['Redo_Stage']}/4]")


def cmd_stats(args: argparse.Namespace) -> None:
    rows = load_rows()
    if not rows:
        print("No entries logged yet in tracker/problem_log.csv.")
        return

    today = dt.date.today()
    week_ago = today - dt.timedelta(days=7)

    total_attempts = len(rows)
    unique_problems = len(latest_by_problem(rows))
    recent = [r for r in rows if r["Date"] >= week_ago.isoformat()]
    medium_times = [int(r["Minutes"]) for r in rows if r["Difficulty"] == "Medium" and r["Minutes"].isdigit()]
    hints = [int(r["Hint_Level"]) for r in rows if r["Hint_Level"].isdigit()]

    fail_by_pattern: Counter[str] = Counter()
    attempts_by_pattern: defaultdict[str, int] = defaultdict(int)
    for r in rows:
        pat = r["Pattern"]
        attempts_by_pattern[pat] += 1
        if r["Result"] == "Failed" or (r["Hint_Level"].isdigit() and int(r["Hint_Level"]) >= 2):
            fail_by_pattern[pat] += 1

    print("=== DSA Journal Stats ===")
    print(f"Unique problems attempted : {unique_problems}")
    print(f"Total attempts (inc. redo): {total_attempts}")
    print(f"Attempts in last 7 days   : {len(recent)}")
    if medium_times:
        print(f"Median Medium time        : {median(medium_times):.1f} min (target: 20-25 min)")
    if hints:
        print(f"Average hint level (0-3)  : {sum(hints) / len(hints):.2f}")

    if fail_by_pattern:
        print("\nWeakest patterns (most failures / hint >= 2):")
        for pat, count in fail_by_pattern.most_common(5):
            print(f"  - {pat}: {count}/{attempts_by_pattern[pat]} struggles")


def main() -> None:
    parser = argparse.ArgumentParser(description="DSA Journal 1-3-7-21 spaced-repetition tracker.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_log = sub.add_parser("log", help="Log a problem attempt")
    p_log.add_argument("--problem", required=True)
    p_log.add_argument("--pattern", required=True)
    p_log.add_argument("--difficulty", required=True, choices=["Easy", "Medium", "Hard"])
    p_log.add_argument("--minutes", required=True, type=int)
    p_log.add_argument("--hint", required=True, type=int, choices=[0, 1, 2, 3])
    p_log.add_argument("--result", required=True, choices=["Clean", "Hint", "Failed"])
    p_log.add_argument("--mistake", default="")
    p_log.add_argument("--date", default="", help="YYYY-MM-DD (defaults to today)")
    p_log.set_defaults(func=cmd_log)

    p_due = sub.add_parser("due", help="Show problems due for redo today")
    p_due.add_argument("--as-of", default="", help="YYYY-MM-DD (defaults to today)")
    p_due.set_defaults(func=cmd_due)

    p_stats = sub.add_parser("stats", help="Show Sunday review statistics")
    p_stats.set_defaults(func=cmd_stats)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
