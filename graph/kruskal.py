import heapq
from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.size = [1] * size
        self.components = size

    def find(self, p: int) -> int:
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p: int, q: int) -> bool:
        rootp = self.find(p)
        rootq = self.find(q)
        if rootq != rootp:
            if self.size[rootp] > self.size[rootq]:
                self.parent[rootq] = self.parent[rootp]
                self.size[rootp] += self.size[rootq]
            else:
                self.parent[rootp] = self.parent[rootq]
                self.size[rootq] += self.size[rootp]
            self.components -= 1
            return True
        return False


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        heap = []
        for source, dest, weight in edges:
            heapq.heappush(heap, [weight, source, dest])
        #
        unionfind = UnionFind(n)
        cost = 0
        while unionfind.components > 1 and heap:
            weight, node1, node2 = heapq.heappop(heap)
            if unionfind.union(node1, node2):
                cost += weight
                
        return cost if unionfind.components == 1 else -1
