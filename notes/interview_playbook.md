# Interview-Day Playbook

Interviewers grade four dimensions: **Communication**, **Problem Solving**, **Technical Competency**, and **Testing**.

---

## The 45-Minute Script

| Minutes | Goal | What to Say |
| :--- | :--- | :--- |
| `0 – 2` | 60-second self-intro | Brief background, 1–2 key builds, what role you're excited about |
| `2 – 8` | Paraphrase, clarify constraints, agree on example | *"Is it sorted? Duplicates? Can I modify in place? Input size limits?"* |
| `8 – 14` | Brute force -> bottleneck -> optimal + green light | *"Brute force is O(n²). A hash map drops this to O(n) time and O(n) space. Sound good?"* |
| `14 – 32` | Code steadily while narrating with clear names | *"I'll write the helper first, then the main loop."* |
| `32 – 40` | Trace example & edge cases before saying "done" | *"Let me trace `[3, 3]` and `[]` to verify my loop bounds."* |
| `40 – 45` | Final Time/Space complexity, trade-offs, your questions | *"With more time I'd add input validation and stress-test the large case."* |

---

## When You Blank (Never Stay Silent > 30s)

1. Say so calmly and restate what you know.
2. Work a small example by hand out loud.
3. Write the brute force — a working slow solution beats silence.
4. Scan the bottleneck: *Hash map? Sorting? Two pointers? Stack? Heap? BFS/DFS?*
5. Ask for a targeted nudge: *"Could you point me toward the data structure I'm missing?"*
6. When given a hint, say *"That helps"*, adopt it immediately, and keep moving.

---

## Universal Edge-Case Checklist

Run through relevant items on every problem before declaring done:
- Empty input (`[]`, `""`, `None`)
- Single element / two elements
- All duplicates / all identical values
- Already sorted / reverse sorted
- Negatives / zeros / very large values
- Strings with spaces, punctuation, mixed case
- Graph cycles, disconnected components, self-loops

---

## Behavioral Round (6 STAR Stories — 90 Seconds Each)

Draft and rehearse your personal stories in `private/behavioral_stories.md` (gitignored):
1. A technical problem you solved and how.
2. A mistake you made and what you changed afterward.
3. A disagreement with a teammate or client, and how it resolved.
4. Working under a deadline or with unclear requirements.
5. A time you took initiative without being asked.
6. Learning something new quickly.

Also prepare:
- Your 60-second self-introduction
- 3 thoughtful questions for the interviewer
- End-to-end explanation of every project on your resume
