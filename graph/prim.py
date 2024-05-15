import heapq
from typing import List, Optional


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        costs = []
        for i in range(n):
            graph[i] = []
        for source, dest, weight in edges:
            graph[source].append((weight, dest))
            graph[dest].append((weight, source))
        for i in graph.keys():
            cost = self._prin(graph, i, n)
            if cost:
                costs.append(cost)
        return min(costs) if costs else -1

    def _prin(self, graph: dict, start: int, nodes: int) -> Optional[int]:
        visited = set()
        cost = 0
        visited.add(start)
        queue = graph[start]
        heapq.heapify(queue)
        while queue:
            weight, dest = heapq.heappop(queue)
            if dest in visited:
                continue
            cost += weight
            visited.add(dest)
            if dest in graph:
                for weight_dest in graph[dest]:
                    heapq.heappush(queue, weight_dest)
        if len(visited) != nodes:
            return None
        return cost
