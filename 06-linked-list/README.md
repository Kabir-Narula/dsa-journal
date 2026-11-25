# 06 — Linked List (Week 4: Dec 21 – Dec 27)

*Holiday week: Mon–Wed work, Dec 24–26 off, Sun Dec 27 = Weeks 1–3 redo sweep.*

**Focus:** Pointer rewiring (`prev` / `cur` / `nxt`), dummy-head trick, fast & slow pointers. Draw boxes and arrows on paper before coding.

## Triggers
- In-place `O(1)` space -> rewire pointers
- Cycle, middle, or k-th from end -> fast/slow or fixed-gap pointers
- Merging or splicing lists -> dummy head node

## Classic Bugs to Watch For
- Overwriting `cur.next` before saving `nxt = cur.next`
- Returning `head` instead of `dummy.next`
- Infinite loops when a cycle exists

## Build From Scratch (`from-scratch/`)
- [ ] Singly Linked List (`append`, `delete`, iterative `reverse`, recursive `reverse`)

## Core Problems (7)
- [ ] Reverse Linked List *(Easy)*
- [ ] Merge Two Sorted Lists *(Easy)*
- [ ] Linked List Cycle *(Easy)*
- [ ] Remove Nth Node From End of List *(Medium)*
- [ ] Reorder List *(Medium)*
- [ ] Add Two Numbers *(Medium)*
- [ ] Copy List with Random Pointer *(Medium)*

## Later in the Plan (4)
- [ ] Find the Duplicate Number *(Floyd's cycle detection)*
- [ ] LRU Cache *(Week 6, after from-scratch build)*
- [ ] Merge k Sorted Lists *(Week 6, with heaps)*
- [ ] Reverse Nodes in k-Group *(Hard — stretch)*

## Personal Notes & Traps
-
