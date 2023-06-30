class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        newnodes = {}

        def dfs(node: Node):
            if node in newnodes:
                return newnodes[node]

            copied = Node(val=node.val)
            newnodes[node] = copied
            for neighbor in node.neighbors:
                n = dfs(neighbors)
                copied.neighbors.append(n)
            return copied

        return dfs(node) if node else None
