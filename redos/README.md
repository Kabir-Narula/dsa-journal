# Spaced-Repetition Redo Workspace (`1-3-7-21`)

> **Rule 4:** Redo beats new. A problem is done only when you re-solve it from a **blank file** in **20 minutes or less**, a week later.

Putting redos in this folder prevents accidentally peeking at your original solution inside the topic folder.

## How to Run Your Morning Warm-Up (20 min)

1. Check what is due today:
   ```bash
   python scripts/tracker_cli.py due
   ```
2. Scaffold a blank redo file:
   ```bash
   python scripts/new_problem.py redo "<Problem Name>" --pattern "<Pattern>" --difficulty Medium
   ```
3. Start a **20-minute timer**. Solve cleanly with no autocomplete and no peeking.
4. Log the outcome (the CLI advances `1 -> 3 -> 7 -> 21 -> Done`, or resets to Day 1 if `> 20 min` or not `Clean`):
   ```bash
   python scripts/tracker_cli.py log --problem "<Problem Name>" --pattern "<Pattern>" --difficulty Medium --minutes 14 --hint 0 --result Clean --mistake "None"
   ```
