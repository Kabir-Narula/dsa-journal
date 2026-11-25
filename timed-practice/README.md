# Timed Practice, Checkpoints & Simulations

The goal is solving **unseen** problems under real time pressure without a topic label.

## Subfolders

- `unseen-transfer/` — Friday unseen problems (Grind 75, 25 min timed, no topic hint) and Saturday transfer tests (Weeks 1, 2, 5).
- `checkpoints/` — Phase gate assessments:
  - **Checkpoint 1 (Sat Dec 19):** 3 unseen Grind 75 problems (1E, 2M), 25m each. Target: `2/3` clean.
  - **Checkpoint 2 (Sat Jan 9):** 3 unseen Mediums (Weeks 4–6), 25m each + recorded explanation.
  - **Checkpoint 3 (Sat Feb 13):** 4 unseen mixed problems in 2 hours. Target: `3/4`.
- `online-assessments/` — Week 12 timed practice OAs on HackerRank, Codility, or CodeSignal (raw `sys.stdin` / `print` I/O).
- `simulations/` — Week 13 full-loop simulations (2 problems in 90 min + 15 min behavioral out loud).

## Quick Scaffold Commands

```bash
python scripts/new_problem.py unseen "Subarray Sum Equals K" --difficulty Medium
python scripts/new_problem.py checkpoint "Checkpoint1_P1" --difficulty Medium
python scripts/new_problem.py oa "OA1_Problem" --difficulty Medium
python scripts/new_problem.py sim "Sim1_P1" --difficulty Medium
```
