# 00 — Pre-Week: Python From Zero (Nov 24 – Nov 29)

Before moving to **Week 1 (`01-arrays-and-hashing`)**, solve and pass all three verification files in this folder **with no AI and no autocomplete**.

---

## Pre-Week Verification Checklist (Pass All 3 Stages to Unlock Week 1)

### Stage 1: Core Python Fluency Drills (`part1_python_drills.py`)
Tests everything from CS50P Lectures 0–4 & 8 + NeetCode's Python interview idioms:
- Functions, conditionals, loops, `try/except`
- List, dict, and set comprehensions
- Strings, slicing, `.split()`, `.join()`
- `sorted(key=...)`, `enumerate()`, `zip()`
- OOP: `ListNode` & `TreeNode` classes + linked list helpers

Run tests:
```powershell
python -m pytest 00-pre-week-python/tests/test_part1_python_drills.py -v
```

### Stage 2: Cold Baseline Retype (`part2_baseline_retype.py`)
Retype the 3 Tuesday baseline problems from memory without looking:
1. `Contains Duplicate`
2. `Two Sum`
3. `Valid Parentheses`

Run tests:
```powershell
python -m pytest 00-pre-week-python/tests/test_part2_baseline.py -v
```

### Stage 3: Official Pre-Week Exit Test (`part3_exit_test.py`) — **THE GATE**
**Rules:** Set a **30-minute timer**. Close all notes, no AI, plain editor.
1. `word_frequencies(text)` — Count word frequencies using a **plain `dict`** (no `Counter`).
2. `reverse_in_place(nums)` — Reverse a list **in place** using **two indices** (no `.reverse()` or `[::-1]`).
3. `ListNode` + `build_three_node_chain(a, b, c)` + `print_chain(head)` — Build a 3-node chain and print each value with a `while` loop.
4. `first_non_repeating_char(s)` — Return the first character that appears exactly once (or `None`).

Run the gate test:
```powershell
python -m pytest 00-pre-week-python/tests/test_part3_exit_test.py -v
```

Run **ALL** Pre-Week tests at once:
```powershell
python -m pytest 00-pre-week-python/tests -v
```

---

## Gate Rule (From Your Roadmap)
- **Pass 4 / 4 on Stage 3 within 30 minutes** -> Check off Pre-Week in `tracker/roadmap_checklist.md`, write your short note in `tracker/weekly_reviews.md`, and start **Week 1 (`01-arrays-and-hashing/`)**!
- **Miss 2 or more** -> Take 2 extra days to drill Python basics before starting Week 1.

---

## Daily Progress Log
- [x] Setup: Python 3, VS Code (interview mode), `dsa-journal` GitHub repo
- [ ] Stage 1 passed (`part1_python_drills.py`)
- [ ] Stage 2 passed (`part2_baseline_retype.py`)
- [ ] Stage 3 passed 4/4 in <= 30 min (`part3_exit_test.py`)
- [ ] One-page card of Python `list`, `dict`, `set`, and string idioms written from memory
