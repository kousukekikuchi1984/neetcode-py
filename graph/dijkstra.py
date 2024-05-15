import heapq


class Solution:
    graph: dict

    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for source, dest, weight in edges:
            adj[source].append([dest, weight])

        shortest = {}
        minheap = [[0, src]]
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, [w1 + w2, n2])
        #
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
