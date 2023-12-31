from typing import Dict, Tuple


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
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

    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if not 0 < r <= rows or not 0 < c <= cols or board[r][c] != "0":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
                else:
                    continue

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                neighbors[pattern].append(word)

        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            res += 1
        return 0

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for ticket in tickets:
            heapq.heappush(graph[ticket[0]], ticket[1])
        #
        result = deque([])

        def dfs(current: str):
            while graph[current]:
                to_airport = heapq.heappop(graph[current])
                dfs(to_airport)
            result.appendleft(current)

        dfs("JFK")
        return result

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        columns = len(matrix[0])
        cache = {}

        def dfs(row: int, column: int) -> int:
            idx = (row, column)
            if row >= rows or column >= columns:
                return 0
            if idx in cache:
                return cache[idx]
            down = dfs(row + 1, column)
            right = dfs(row, column + 1)
            diag = dfs(row + 1, column + 1)
            cache[idx] = 0
            if matrix[row][column] == "1":
                side_length = 1 + min(down, right, diag)
                cache[idx] = side_length
            return cache[idx]

        dfs(0, 0)
        return max(cache.values()) ** 2

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(src: int, dest: int, seen: Dict[int, bool]) -> bool:
            if src == dest:
                return True
            if src in seen:
                return seen[src]
            childs = []
            for node in adj[src]:
                child = dfs(node, dest, seen)
                childs.append(child)
            result = any(childs)
            seen[src] = result
            return result

        adj = {n: [] for n in range(numCourses)}
        for prerequisite in prerequisites:
            adj[prerequisite[0]].append(prerequisite[1])
        #
        results = []
        for query in queries:
            result = dfs(query[0], query[1], {})
            results.append(result)
        return results

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = collections.defaultdict(list)
        blue = collections.defaultdict(list)

        for src, dst in redEdges:
            red[src].append(dst)
        for src, dst in blueEdges:
            blue[src].append(dst)

        answer = [-1 for _ in range(n)]
        answer[0] = 0
        q = deque()
        q.append([0, 0, None])
        visit = set()
        visit.add((0, None))
        while q:
            node, length, color = q.popleft()
            if answer[node] == -1:
                answer[node] = length

            if color != "RED":
                for nei in red[node]:
                    if (nei, "RED") not in visit:
                        visit.add(nei, "RED")
                        q.append((nei, length + 1, "RED"))

            if color != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visit:
                        visit.add(nei, "BLUE")
                        q.append((nei, length + 1, "BLUE"))

        return answer

    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs approach
        visit = set()
        never = set(deadends)
        plus = {str(i): str((i + 1) % 10) for i in range(10)}
        minus = {str(i): str((i - 1) % 10) for i in range(10)}
        queue = ["0000"]
        result = 0
        while queue:
            result += 1
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur in never:
                    continue
                if cur in visit:
                    continue
                if cur == target:
                    return result
                visit.add(cur)
                for i in range(4):
                    next_plus = cur[:i] + plus[cur[i]] + cur[i+1:]
                    queue.append(next_plus)
                    next_minus = cur[:i] + minus[cur[i]] + cur[i+1:]
                    queue.append(next_minus)
        return -1

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            nxtPair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nxtPair
            prev.next = second

            # update ptrs
            prev = curr
            curr = nxtPair
        return dummy.next
