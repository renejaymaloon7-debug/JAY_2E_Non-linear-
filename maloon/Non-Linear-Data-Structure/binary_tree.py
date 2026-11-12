r"""
Binary Tree structure (from the diagram)

            M
          /   \
         A     L
        / \     \
      O1   O2    N

Traversals:
    BFS (level order): M -> A -> L -> O1 -> O2 -> N
    DFS (preorder)   : M -> A -> O1 -> O2 -> L -> N
"""
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def bfs(self):
        """Breadth-first (level order) using a queue."""
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs(self):
        """Depth-first (preorder: root, left, right) using recursion."""
        result = []
        self._dfs(self.root, result)
        return result

    def _dfs(self, node, result):
        if node is None:
            return
        result.append(node.value)
        self._dfs(node.left, result)
        self._dfs(node.right, result)

    def display(self):
        """Print each node with its children."""
        if self.root is None:
            print("(empty tree)")
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            left = node.left.value if node.left else "-"
            right = node.right.value if node.right else "-"
            print(f"{node.value}: left={left}, right={right}")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def build_sample_tree():
    m, a, l = Node("M"), Node("A"), Node("L")
    o1, o2, n = Node("O1"), Node("O2"), Node("N")

    m.left, m.right = a, l
    a.left, a.right = o1, o2
    l.left = n
    return BinaryTree(m)


if __name__ == "__main__":
    tree = build_sample_tree()
    print("=== BINARY TREE ===")
    tree.display()
    print("BFS:", " -> ".join(tree.bfs()))
    print("DFS:", " -> ".join(tree.dfs()))
