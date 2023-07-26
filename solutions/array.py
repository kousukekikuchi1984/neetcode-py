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

    def isSubsequence(self, s: str, t: str) -> bool:
        cur_s = cur_t = 0
        while cur_s < len(s) and cur_t < len(t):
            if s[cur_s] == t[cur_t]:
                cur_s += 1
                cur_t += 1
            else:
                cur_t += 1
        return cur_s == len(s)

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])

    def longestCommonPrefix(self, strs: List[str]) -> str:
        results = ""
        for s in zip(*strs):
            if len(set(s)) == 1:
                results += s[0]
            else:
                break
        return results

    def generate(self, numRows: int) -> List[List[int]]:
        results = [[1]]
        for _ in range(numRows - 1):
            prev = results[-1]
            current = []
            cursor = 0
            while cursor <= len(prev):
                left = 0 if cursor - 1 < 0 else prev[cursor - 1]
                right = 0 if cursor == len(prev) else prev[cursor]
                val = left + right
                current.append(val)
                cursor += 1
            results.append(current)
        return results
