class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        heapq.heapify(nums)

        previous = 0
        minimum = float("inf")
        maximum = 0
        missing = None
        while nums:
            current = heapq.heappop(nums)
            if current < 1:
                continue
            if minimum == float("inf"):
                if current != 1:
                    return 1
                minimum = float("inf")
            if previous + 1 != current:
                return previous + 1
            maximum = max(current, maximum)
        return maximum

    def replaceElements(self, arr: List[int]) -> List[int]:
        results = [-1]
        length = len(arr)
        for i in range(1, length):
            index = length - i
            value = max(results[0], arr[index - 1])
            results.insert(0, value)
        return results
