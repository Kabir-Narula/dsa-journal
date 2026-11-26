# Build From Scratch

Hand-implementing core data structures and algorithms once (30–45 minutes each, no stdlib shortcuts) builds real recall and prepares you for interviewers who disallow built-in helpers.

Use `python scripts/new_problem.py scratch "<Structure Name>"` to start a fresh file.

---

## Weekly Build Checklist

### Week 1
- [ ] Frequency counter using a plain `dict` (no `collections.Counter`)
- [ ] Tiny Hash Map with chaining (list of buckets)
- [ ] Dynamic Array (NeetCode Core Skills)
- [ ] Singly Linked List (NeetCode Core Skills)

### Week 2
- [ ] Read/write pointer in-place edit (remove all occurrences of one value from a list)
- [ ] Valid-parentheses checker using a `list` as a stack
- [ ] Monotonic stack hand-trace (`[73, 74, 75, 71, 69, 72, 76, 73]`)
- [ ] Double-ended Queue / Deque (NeetCode Core Skills)

### Week 3
- [ ] Binary Search from memory (on 3 different days)
- [ ] Variable Sliding Window template from memory

### Week 4
- [ ] Singly Linked List (`append`, `delete`, iterative `reverse`, recursive `reverse`)

### Week 5
- [ ] Binary Tree DFS traversals: Pre-order, In-order, Post-order (recursive & iterative with explicit stack)
- [ ] Level-order BFS with `deque`
- [ ] Local test helper `build_tree([1, 2, 3, None, 4])`
- [ ] Binary Search Tree (NeetCode Core Skills)

### Week 6
- [ ] Min-Heap with `sift_up` and `sift_down` on a plain `list`
- [ ] Trie class (`insert`, `search`, `starts_with`)
- [ ] LRU Cache (1: `dict` + doubly linked list, 2: `collections.OrderedDict`)

### Week 7
- [ ] Backtracking `subsets` and `permutations` from memory (on 2 different days)

### Week 8
- [ ] Graph BFS & DFS (both recursive and iterative)
- [ ] Kahn's Algorithm (topological sort via in-degree + queue)
- [ ] Union-Find (path compression + union by size)

### Week 9
- [ ] Dijkstra's shortest path with `heapq`
- [ ] Fibonacci 4 ways: plain recursion -> `@cache` memoization -> bottom-up table -> `O(1)` space

### Core Sorting (Anytime Weeks 1–6)
- [ ] Merge Sort
- [ ] Quicksort Partition
