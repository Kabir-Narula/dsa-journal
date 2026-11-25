# DSA Journal — 3-Month Python Coding Interview Roadmap

A structured, pattern-first Python Data Structures & Algorithms study repository covering a 13-week interview preparation roadmap (Nov 24, 2026 – Feb 28, 2027): **NeetCode 150**, from-scratch data structure implementations, **1-3-7-21 spaced-repetition redos**, unseen transfer problems, and timed mock simulations.

---

## Core Rules

1. **No AI before minute 45.** Struggle is the mechanism that builds recall.
2. **Plain editor, autocomplete off.** `.vscode/settings.json` disables inline suggestions and IntelliSense in this workspace to mirror live interview editors.
3. **Pattern first, problem second.** Every solved problem is tagged with its pattern and one-line trigger.
4. **Redo beats new.** A problem is only "done" once re-solved cleanly from a blank file in `<= 20` minutes a week later (`1 → 3 → 7 → 21` day schedule).
5. **Narrate out loud.** Talk through constraints, brute force, bottleneck, implementation, and edge cases on every session.
6. **Mock early and weekly from Week 7.** Target 12+ mocks total (at least 4 with a human interviewer).

---

## Roadmap Overview (4 Phases, 4 Gates)

| Phase | Weeks | Dates | Focus | Gate / Checkpoint |
| :--- | :--- | :--- | :--- | :--- |
| **Pre-Week** | 0 | Nov 24 – Nov 29 | Python from zero (`CS50P`, built-ins, OOP) | 30-min blank Exit Test (4/4) |
| **Phase 1** | 1 – 3 | Nov 30 – Dec 20 | Arrays & Hashing, Two Pointers, Stack, Binary Search, Sliding Window | **Checkpoint 1 (Dec 19):** 3 unseen Grind 75 problems (1E, 2M), 25m each |
| **Phase 2** | 4 – 7 | Dec 21 – Jan 17 | Linked Lists, Trees, Heaps, Tries, Backtracking | **Checkpoint 2 (Jan 9):** 3 unseen Mediums + recorded explanation; **Mock #1 (Jan 16)** |
| **Phase 3** | 8 – 11 | Jan 18 – Feb 14 | Graphs, Advanced Graphs, 1-D & 2-D DP, Greedy, Intervals, Bits | **Checkpoint 3 (Feb 13):** 4 unseen mixed problems in 2 hours |
| **Phase 4** | 12 – 13 | Feb 15 – Feb 28 | Math & Matrix, Weak-Spot Repair, Online Assessments, Full-Loop Simulations | **Ready Benchmark (Feb 28):** Unseen Easy 10–12m, Unseen Medium 20–25m |

---

## Repository Structure

```text
dsa-journal/
├── 00-pre-week-python/          # Pre-week Python drills, baseline & Exit Test
├── 01-arrays-and-hashing/       # Week 1: Arrays, Hashing, Big-O (9 + 2 transfer)
├── 02-two-pointers/             # Week 2: Converging & read/write pointers (5 + 2 transfer)
├── 03-stack/                    # Week 2: Stack & monotonic stack (7)
├── 04-binary-search/            # Week 3: Index & answer-space binary search (7)
├── 05-sliding-window/           # Week 3: Fixed & variable windows (6)
├── 06-linked-list/              # Week 4: Pointer rewiring, fast/slow, dummy head (11)
├── 07-trees/                    # Week 5: DFS, BFS, BST recursion (15 + 3 transfer)
├── 08-heap-and-priority-queue/  # Week 6: Top-K, running median, scheduling (7)
├── 09-tries/                    # Week 6: Prefix trees (3)
├── 10-backtracking/             # Week 7: Decision trees, subsets, permutations (9)
├── 11-graphs/                   # Week 8: Grid BFS/DFS, topological sort, union-find (13)
├── 12-advanced-graphs/          # Week 9: Dijkstra, MST, Bellman-Ford (6)
├── 13-1d-dynamic-programming/   # Weeks 9–10: Linear recurrences & memoization (12)
├── 14-2d-dynamic-programming/   # Week 10: Grid, string & knapsack DP (6)
├── 15-greedy/                   # Week 11: Local-choice proofs & intervals prep (8)
├── 16-intervals/                # Week 11: Sorting & sweeping intervals (6)
├── 17-bit-manipulation/         # Week 11: XOR, bitmasks & shifts (5)
├── 18-math-and-matrix/          # Week 12: Matrix traversal & math primitives (7)
├── from-scratch/                # Hand-implemented data structures & core algorithms
├── redos/                       # Blank-file workspace for 1-3-7-21 spaced redos
├── timed-practice/              # Checkpoints, Friday unseen transfer, OAs, full simulations
├── notes/                       # Python toolkit, pattern index cards & interview playbook
├── tracker/                     # Problem CSV log, 13-week checklist, Sunday reviews, mocks
├── templates/                   # 6-step problem loop Python starter template
└── scripts/                     # Zero-dependency CLI helpers for scaffolding & redo tracking
```

---

## Daily & Weekly Workflow

### Daily 4-Hour Session (Mon – Thu)
| Block | Time | Activity |
| :--- | :--- | :--- |
| **Recall Warm-Up** | 20 min | Re-solve 1–2 due problems from the `1-3-7-21` queue in `redos/` (blank file) |
| **Learn** | 45 min | Study the day's concept and code the structure/template in `from-scratch/` |
| **Deep Practice 1** | 60 min | New problem following the 6-step loop & stuck ladder |
| **Break** | 10–15 min | Step away from the screen |
| **Deep Practice 2** | 60 min | New problem (25-min timed attempt starting Week 4) |
| **Wrap-Up** | 25 min | Update `tracker/problem_log.csv`, update pattern card, 2-min out-loud recap |

### Weekly Rhythm
- **Mon – Thu:** New-topic sessions.
- **Fri (Mixed Day):** Clear redo queue + 1 unseen problem (25 min timed, no topic label) in `timed-practice/unseen-transfer/`.
- **Sat (Interview Day):** 2 timed problems back-to-back (45 min each) + mock interview (Week 7+) + error log review.
- **Sun (Off):** Rest. At most 1 hour of light pattern-card review and Sunday check-in (`tracker/weekly_reviews.md`).

---

## Quick CLI Helpers

Requires Python 3 (zero external dependencies).

### 1. Scaffold a new problem (with the 6-step loop template)
```bash
python scripts/new_problem.py 01 "Two Sum" --difficulty Easy --url "https://leetcode.com/problems/two-sum/"
```

### 2. Scaffold a blank redo file (in `redos/` so you don't peek at old code)
```bash
python scripts/new_problem.py redo "Two Sum" --pattern "Arrays & Hashing" --difficulty Easy
```

### 3. Log an attempt & auto-schedule 1-3-7-21 spaced repetition
```bash
python scripts/tracker_cli.py log --problem "Two Sum" --pattern "Arrays & Hashing" --difficulty Easy --minutes 18 --hint 0 --result Clean --mistake "Handled duplicate index edge case"
```

### 4. Check today's due redos & Sunday review stats
```bash
python scripts/tracker_cli.py due
python scripts/tracker_cli.py stats
```

---

## Stuck Ladder (Time-Boxed)

| Minute | Action |
| :--- | :--- |
| `0 – 5` | Understand problem, write 2 examples & edge cases |
| `5 – 25` | Brute force -> optimize (no hints, no AI) |
| `25` | **Hint 1:** Topic tag only -> try 10 more minutes |
| `35` | **Hint 2:** High-level idea only (no code) -> implement yourself |
| `45` | Study full solution -> close it -> type from memory today & tomorrow -> log as `Failed` |

---

## Progress Snapshot

- **Master Checklist:** [`tracker/roadmap_checklist.md`](tracker/roadmap_checklist.md)
- **Spaced-Repetition Log:** [`tracker/problem_log.csv`](tracker/problem_log.csv)
- **Weekly Sunday Reviews:** [`tracker/weekly_reviews.md`](tracker/weekly_reviews.md)
- **Mock Interview Log:** [`tracker/mock_log.md`](tracker/mock_log.md)
- **Python Toolkit & Gotchas:** [`notes/python_toolkit.md`](notes/python_toolkit.md)
- **Pattern Trigger Cards:** [`notes/pattern_cards.md`](notes/pattern_cards.md)
- **Interview-Day Playbook:** [`notes/interview_playbook.md`](notes/interview_playbook.md)
