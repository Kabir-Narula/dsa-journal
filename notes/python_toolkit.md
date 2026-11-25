# Python Interview Toolkit

Master these built-in complexities, idioms, and pitfalls in Week 1 so syntax never slows you down in interviews.

---

## Built-In Time Complexities

| Operation | Complexity | Notes |
| :--- | :--- | :--- |
| `list` index, `append()`, `pop()` (end) | `O(1)` | `append` is amortized |
| `list` insert/delete at front/middle, `x in list` | `O(n)` | Shifts elements |
| `list` / `str` slice `a[i:j]` | `O(k)` | Copies slice of length `k` |
| `str` or `tuple` edit | `O(n)` | Immutable — creates a new object |
| `dict` get/set/delete; `set` add/remove/lookup | `O(1)` avg | Hash table |
| `deque` `append`/`appendleft`/`pop`/`popleft` | `O(1)` | Always use for BFS queues |
| `sorted()`, `list.sort()` | `O(n log n)` | Timsort (stable) |
| `heapq.heappush`, `heapq.heappop` | `O(log n)` | Min-heap by default |
| `heapq.heapify` | `O(n)` | Linear time in-place |
| `heapq.nlargest(k, ...)` | `O(n log k)` | Heap of size `k` |
| `bisect_left`, `bisect_right` | `O(log n)` | Binary search on sorted list |
| `bisect.insort` | `O(n)` | `O(log n)` search + `O(n)` shift |

---

## High-Frequency Standard Library Snippets

```python
from collections import Counter, defaultdict, deque
import heapq
import bisect
from functools import cache

# Counting & grouping
cnt = Counter("banana")           # Counter({'a': 3, 'n': 2, 'b': 1})
groups = defaultdict(list)        # groups[key].append(x) without key checks
adj = defaultdict(list)           # graph adjacency list

# BFS Queue (never use list.pop(0))
q = deque([start])
node = q.popleft()

# Heap (min-heap; negate values for max-heap)
h = []
heapq.heappush(h, (dist, node))   # tuples compare left to right
dist, node = heapq.heappop(h)

# Binary search helpers
i = bisect.bisect_left(a, x)      # first index where a[i] >= x
j = bisect.bisect_right(a, x)     # first index where a[j] > x

# Memoization (arguments must be hashable: tuples, not lists)
@cache
def dp(i, j):
    ...

# Sorting with custom keys
intervals.sort(key=lambda x: x[0])
people.sort(key=lambda p: (-p.score, p.name))

# Common idioms
INF = float("inf")
a, b = b, a
text = "".join(parts)             # never build strings with += in a loop
ord("a"), chr(97), s[::-1]
for i, x in enumerate(arr): ...
for x, y in zip(a, b): ...
```

---

## Standard Node Definitions

CoderPad and HackerRank often require writing these yourself:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## Online Assessment Standard Input (HackerRank / Codility / CodeSignal)

```python
import sys

data = sys.stdin.read().split()
# Or line-by-line:
# line = input().strip()
```

---

## Python Interview Gotchas

1. **List as a queue:** `list.pop(0)` is `O(n)` and turns BFS quadratic. Always use `collections.deque`.
2. **Nested list aliasing:** `[[0] * 3] * 2` shares row references. Use `[[0] * 3 for _ in range(2)]`.
3. **Mutable default args:** `def f(x, seen=[]):` persists across calls. Default to `None`.
4. **Appending a mutated list:** In backtracking, use `res.append(path[:])`, never `res.append(path)`.
5. **Mutating a dict during iteration:** Raises `RuntimeError`. Iterate over `list(d)`.
6. **Negative floor division & modulo:** `-7 // 2 == -4` and `-7 % 3 == 2` (truncation toward zero: `int(-7 / 2) == -3`).
7. **Recursion limit:** Default is ~1,000 frames. Deep trees/lists need `sys.setrecursionlimit` or an iterative stack.
8. **Slicing inside recursion:** `nums[1:]` copies `O(n)` per call. Pass index `i` instead.
9. **`range` end is exclusive:** Counting down to `0` inclusive is `range(n, -1, -1)`.
10. **Float equality:** `0.1 + 0.2 == 0.3` is `False`. Prefer integers or `math.isclose`.
11. **Arbitrary-precision ints in bit problems:** Python ints do not overflow at 32 bits; mask with `0xFFFFFFFF` when simulating 32-bit integers.
