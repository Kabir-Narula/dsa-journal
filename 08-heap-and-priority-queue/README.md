# 08 — Heap & Priority Queue (Week 6: Jan 4 – Jan 10)

**Focus:** `heapq` is a min-heap (negate values for max-heap); size-`k` heap gives top `k` in `O(n log k)`; two heaps track a running median.

## Triggers
- *"k largest, smallest, or most frequent"* -> heap of size `k`
- *"Repeatedly take the min or max"* -> priority queue / heap
- *"Median of a stream"* -> two heaps (max-heap lower half + min-heap upper half)

## Build From Scratch (`from-scratch/`)
- [ ] Min-Heap with `sift_up` and `sift_down` on a plain `list`
- [ ] LRU Cache (`dict` + doubly linked list, then `OrderedDict`)

## NeetCode 150 Problems (7)
- [ ] Kth Largest Element in a Stream *(Easy)*
- [ ] Last Stone Weight *(Easy)*
- [ ] K Closest Points to Origin *(Medium)*
- [ ] Kth Largest Element in an Array *(Medium)*
- [ ] Task Scheduler *(Medium)*
- [ ] Design Twitter *(Medium)*
- [ ] Find Median from Data Stream *(Hard — stretch)*

## Also Complete This Week
- [ ] Merge k Sorted Lists *(Heap problem in `06-linked-list/`)*
- [ ] LRU Cache *(in `06-linked-list/`)*

## Gate — Checkpoint 2 (Sat Jan 9)
- [ ] 3 unseen Mediums across Weeks 4–6 (25 min each) + record yourself explaining one solution aloud

## Personal Notes & Traps
-
