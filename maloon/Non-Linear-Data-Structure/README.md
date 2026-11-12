# Non-Linear Data Structure

Python programs for the two diagrams: a **binary tree** and a **graph**.
Each one has a BFS and a DFS traversal.

## Files
| File | Description |
|------|-------------|
| `binary_tree.py` | Binary tree (M, A, L, O1, O2, N) with BFS and DFS (preorder) |
| `graph.py` | Undirected graph (M, A, L, O1, O2, N) with BFS and DFS |
| `main.py` | Runs both programs |

## Diagrams
**Binary tree:** M -> (A, L), A -> (O1, O2), L -> N

**Graph edges:** M-A, M-L, A-O1, A-O2, O1-O2, O2-N, L-N

## How to run
```
python main.py
```

## Output
```
=== BINARY TREE ===
M: left=A, right=L
A: left=O1, right=O2
L: left=N, right=-
O1: left=-, right=-
O2: left=-, right=-
N: left=-, right=-
BFS: M -> A -> L -> O1 -> O2 -> N
DFS: M -> A -> O1 -> O2 -> L -> N

=== GRAPH ===
M: A, L
A: M, O1, O2
L: M, N
O1: A, O2
O2: A, O1, N
N: O2, L
BFS: M -> A -> L -> O1 -> O2 -> N
DFS: M -> A -> O1 -> O2 -> N -> L
```
