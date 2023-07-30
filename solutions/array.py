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

    def numUniqueEmails(self, emails: List[str]) -> int:
        cur = 0
        while cur < len(emails):
            email = emails[cur]
            local, domain = email.split("@")
            local = local.replace(".", "")
            local = local.split("+")[0]
            emails[cur] = f"{local}@{domain}"
            cur += 1
        return set(emails)

    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(nums, key=lambda x: int(x))
        return nums[-k]

    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # char: count

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:
                stack.pop()

        result = ""
        for c in stack:
            result += c[0] * c[1]
        return result

    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = total = nums[0]

        for i in range(1, len(nums)):
            total += nums[i]
            result = max(result, math.ceil(total / (i + 1)))

        return result

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 1
        for placed in flowerbed:
            if placed == 0:
                count += 1
            else:
                n -= int((count - 1) / 2)
                count = 0
        n -= empty // 2
        return n <= 0

    def minFlipsMonoIncr(self, s: str) -> int:
        left = 0
        first_distance = len([c for c in s if c == "0"])
        min_distance = first_distance
        right = first_distance
        for i in range(len(s)):
            c = s[i]
            if c == "1":
                left += 1
            else:
                right -= 1
            min_distance = min(min_distance, left + right)
        return min_distance
