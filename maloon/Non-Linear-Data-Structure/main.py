from binary_tree import build_sample_tree
from graph import build_sample_graph


def main():
    tree = build_sample_tree()
    print("=== BINARY TREE ===")
    tree.display()
    print("BFS:", " -> ".join(tree.bfs()))
    print("DFS:", " -> ".join(tree.dfs()))

    print()

    graph = build_sample_graph()
    print("=== GRAPH ===")
    graph.display()
    print("BFS:", " -> ".join(graph.bfs("M")))
    print("DFS:", " -> ".join(graph.dfs("M")))


if __name__ == "__main__":
    main()
