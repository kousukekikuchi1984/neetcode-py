from collections import Counter
from typing import List
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0

        while heap or queue:
            time += 1
            if not heap:
                time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time
