from copy import deepcopy
from collections import defaultdict


class Graph:
    
    def __init__(self):
        self.paths = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.paths[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if dst in self.paths[src]:
            self.paths[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        paths = deepcopy(self.paths)
        def _dfs(src: int) -> bool:
            if dst in paths[src]:
                return True
            results = []
            for edge in paths[src]:
                result = _dfs(edge)
                results.append(result)
            del paths[src]
            return any(results)
                
        return _dfs(src)
