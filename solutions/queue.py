class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        result, heap = [], []
        cur_task_index = 0
        cur_time = tasks[0][0]
        
        while len(result) < len(tasks):
            while (cur_task_index < len(tasks)) and (tasks[cur_task_index][0] <= cur_time):
                heapq.heappush(heap, (tasks[cur_task_index][1], tasks[cur_task_index][2]))
                cur_task_index += 1
            if heap:
                time_difference, original_index = heapq.heappop(heap)
                cur_time += time_difference
                result.append(original_index)
            elif cur_task_index < len(tasks):
                cur_time = tasks[cur_task_index][0]
                
        return result

    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        queue = []
        for char, count in counter.items():
            heapq.heappush(queue, (-count, char))

        prev = None
        result = ""
        while queue:
            cur = heapq.heappop(queue)
            if result and cur[1] == result[-1]:
                return ""
            result += cur[1]
            if prev:
                heapq.heappush(queue, prev)
            prev = (cur[0] + 1, cur[1]) if cur[0] + 1 != 0 else None
        return result if prev is None else ""
