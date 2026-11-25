# Pattern Index Cards

Maintain one concise card per pattern: **When I see this -> think that**, plus your own 8-line template and common traps as you complete each week.

| Pattern | Trigger ("When I see...") | Core Structure / Technique | Common Traps |
| :--- | :--- | :--- | :--- |
| **Arrays & Hashing** | Seen before / duplicate / frequency; pair summing to target; group by canonical form; top-k frequency | `set`, `dict` (complement lookup), sorted string or count tuple key, bucket sort | Using same index twice; mutating dict while iterating |
| **Two Pointers** | Sorted array + pair/triple; palindrome; in-place array compaction | Converging `l, r` or read/write pointers | Duplicate skipping in 3Sum; wrong pointer advancement |
| **Stack / Monotonic Stack** | Matching brackets / nesting; "next greater / smaller element" | `list` stack storing values or indices | Forgetting to check stack non-empty before `stack[-1]` |
| **Binary Search** | Sorted/rotated array + `O(log n)`; "minimum X such that `feasible(X)`" | `lo <= hi`, `mid = (lo + hi) // 2` | Off-by-one loop condition; infinite loop on `lo = mid` |
| **Sliding Window** | Contiguous subarray/substring with constraint | Grow `right`, shrink `left` while invalid | Updating best before window is valid; forgetting to remove `s[left]` |
| **Linked List** | In-place `O(1)` space; cycle/middle/k-th from end; merging/splicing | `prev/cur/nxt` rewiring, fast/slow pointers, dummy head | Overwriting `cur.next` before saving; returning `head` instead of `dummy.next` |
| **Trees** | Any hierarchy / subtree query; level-by-level / shortest depth; BST ordering | Recursive DFS (return value + nonlocal best), BFS with `deque` | Missing `None` base case; confusing node vs subtree return value |
| **Heap / Priority Queue** | Top-k largest/smallest/frequent; repeatedly take min/max; running median | `heapq` size-`k` heap; two heaps (max + min) | Forgetting Python's `heapq` is min-only (negate for max) |
| **Tries** | Prefix search, autocomplete, word dictionary with wildcards | Nested dict / `TrieNode` children + `is_end` | Forgetting `is_end` check in `search` vs `starts_with` |
| **Backtracking** | All combinations, permutations, subsets; small `n <= 20` | Choose -> explore -> un-choose; sort + skip equal siblings | Appending `path` instead of `path[:]` |
| **Graphs** | Grid regions; fewest unweighted steps; multi-source spread; prerequisites; connectivity | Flood fill DFS/BFS, multi-source BFS, Kahn's topo sort, Union-Find | Marking visited on pop instead of push; deep recursion limit on grids |
| **Advanced Graphs** | Weighted shortest path; MST; limited stops | Dijkstra (`heapq`), Prim/Kruskal, Bellman-Ford | Skipping stale heap entries (`if d > dist[u]: continue`) |
| **1-D & 2-D DP** | Overlapping subproblems + min/max/count/feasibility; 2-string compare; knapsack budget | State in words -> recurrence -> base cases -> `@cache` -> table | Wrong base case; mutating state or non-hashable `@cache` args |
| **Greedy** | Locally optimal choice provably never hurts | Sort + single pass / running max or min | Assuming greedy works without checking counterexample |
| **Intervals** | Overlap, merge, schedule, minimum meeting rooms | Sort by start (or end for max non-overlapping); min-heap of end times | Boundary equality (`end <= next_start` vs `<`) |
| **Bit Manipulation** | Every element appears twice except one; set-bit count; power of 2 | XOR (`a ^ a == 0`), `n & (n - 1)`, bit shifts | Python negative numbers & 32-bit mask `0xFFFFFFFF` |
| **Math & Matrix** | In-place rotation, spiral bounds, zero propagation | Layer/boundary pointers (`top, bottom, left, right`), transpose + reverse | Aliasing rows; boundary crossing mid-loop |

---

## Five Templates to Write Blind by Week 4

Practice writing these from memory in `from-scratch/` until you can reproduce all five cleanly without looking:
1. Binary Search (`lo <= hi`)
2. Variable Sliding Window (longest substring without repeats)
3. Grid BFS (`deque` + `seen` on push)
4. Recursive Tree DFS (`max_depth` / post-order)
5. Backtracking (`subsets` take/skip with `path[:]`)
