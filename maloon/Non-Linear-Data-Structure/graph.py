"""
Graph structure (from the diagram)

Vertices: M, A, L, O1, O2, N
Edges   : M-A, M-L, A-O1, A-O2, O1-O2, O2-N, L-N
"""
from collections import deque


class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, a, b):
        """Undirected edge."""
        self.add_vertex(a)
        self.add_vertex(b)
        self.adj[a].append(b)
        self.adj[b].append(a)

    def display(self):
        for v, neighbors in self.adj.items():
            print(f"{v}: {', '.join(neighbors)}")

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        order = []
        while queue:
            v = queue.popleft()
            order.append(v)
            for nb in self.adj[v]:
                if nb not in visited:
                    visited.add(nb)
                    queue.append(nb)
        return order

    def dfs(self, start):
        visited = set()
        order = []
        self._dfs(start, visited, order)
        return order

    def _dfs(self, v, visited, order):
        visited.add(v)
        order.append(v)
        for nb in self.adj[v]:
            if nb not in visited:
                self._dfs(nb, visited, order)


def build_sample_graph():
    g = Graph()
    for v in ["M", "A", "L", "O1", "O2", "N"]:
        g.add_vertex(v)
    g.add_edge("M", "A")
    g.add_edge("M", "L")
    g.add_edge("A", "O1")
    g.add_edge("A", "O2")
    g.add_edge("O1", "O2")
    g.add_edge("O2", "N")
    g.add_edge("L", "N")
    return g


if __name__ == "__main__":
    g = build_sample_graph()
    print("=== GRAPH ===")
    g.display()
    print("BFS:", " -> ".join(g.bfs("M")))
    print("DFS:", " -> ".join(g.dfs("M")))
