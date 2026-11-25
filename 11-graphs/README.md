# 11 — Graphs (Week 8: Jan 18 – Jan 24)

**Focus:** Adjacency lists (`defaultdict(list)`), grids as implicit graphs, BFS for shortest unweighted paths, DFS for connected regions, cycle detection, topological sort, and Union-Find.

## Triggers
- Grid with connected regions -> flood fill (DFS or BFS)
- Fewest steps in unweighted graph -> BFS
- Spreads from many sources simultaneously -> multi-source BFS (push all sources into queue first)
- Prerequisites / dependency ordering -> topological sort (Kahn's BFS or DFS post-order)
- *"Are these connected?"* / *"which edge is redundant?"* -> Union-Find

## Watch For
- Always mark `visited` **when pushing** to the BFS queue, not when popping.
- Deep recursive DFS on large grids can hit Python's recursion limit (~1,000 frames).

## Build From Scratch (`from-scratch/`)
- [ ] Graph BFS & DFS (recursive and iterative)
- [ ] Kahn's algorithm for topological sort
- [ ] Union-Find with path compression & union by size

## NeetCode 150 Problems (13)
- [ ] Number of Islands *(Medium)*
- [ ] Clone Graph *(Medium)*
- [ ] Max Area of Island *(Medium)*
- [ ] Pacific Atlantic Water Flow *(Medium)*
- [ ] Surrounded Regions *(Medium)*
- [ ] Rotting Oranges *(Medium)*
- [ ] Walls and Gates *(Medium)*
- [ ] Course Schedule *(Medium)*
- [ ] Course Schedule II *(Medium)*
- [ ] Redundant Connection *(Medium)*
- [ ] Number of Connected Components in an Undirected Graph *(Medium)*
- [ ] Graph Valid Tree *(Medium)*
- [ ] Word Ladder *(Hard — stretch)*

## Personal Notes & Traps
-
