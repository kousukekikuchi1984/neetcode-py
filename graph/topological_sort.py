from typing import List
from collections import deque, defaultdict


class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            in_degree[end] += 1
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        topological_order = []
        while queue:
            node = queue.popleft()
            topological_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)


        if len(topological_order) == n:
            return topological_order
        return []
