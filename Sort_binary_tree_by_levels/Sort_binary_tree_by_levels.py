def tree_by_levels(node):
    visited = []
    que = [node]
    if node is not None and node.value is not None:
        while que:
            current_node = que.pop(0)
            if isinstance(current_node, Node):
                que.append(current_node.left)
                que.append(current_node.right)
                visited.append(current_node.value)
    return visited

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value}'


first_tree = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)
print(tree_by_levels(first_tree))
print(tree_by_levels(None))
