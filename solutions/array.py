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

    def arraySign(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                count += 1
        return 1 if count % 2 == 0 else -1

    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))

    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return True

        changed = False
        for i, num in enumerate(nums):
            if i == len(nums) - 1 or num <= nums[i + 1]:
                continue
            if changed:
                return False
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            changed = True
        return True

    def gridGame(self, grid: List[List[int]]) -> int:
        result = float("inf")
        left, right = 0, sum(grid[0])
        for a, b in zip(grid[0], grid[1]):
            right -= a
            result = min(result, max(left, right))
            left += b
        return result

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        def util(i: int, j: int) -> bool:
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return util(i + 1, j) or util(i, j - 1)
        return True

    def rotate(self, nums: List[int], k: int) -> None:
        copied = nums.copy()
        for i in range(len(nums)):
            index = i + k
            nums[i] = copied[index % len(nums)]

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        before = nums[:n]
        after = nums[n:]
        for i in range(n):
            nums[i * 2] = before[i]
            nums[i * 2 + 1] = after[i]
        return nums

    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag = 0
        n = len(mat)
        for i in range(n):
            diag += mat[i][i]
            if i == n - i - 1:
                continue
            diag += mat[n - i - 1][i]
        return diag

    def maxAlternatingSum(self, nums: List[int]) -> int:
        result = 0
        prev = nums[0]
        used_as_plus = True
        for i in range(1, len(nums)):
            if used_as_plus and nums[i] <= nums[i - 1]:
                result += prev
                used_as_plus = False
            elif not used_as_plus and nums[i] >= nums[i - 1]:
                result -= prev
                used_as_plus = True
            prev = nums[i]
        if used_as_plus:
            result += prev
        return result

    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cur = 0
        while cur + 1 < len(nums):
            left = nums[cur]
            right = nums[cur + 1]
            if left != right:
                return left
            cur = cur + 2
        return nums[cur]

    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1

        return True

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def is_divosor(length) -> bool:
            if len1 % length or len2 % length:
                return False
            f1, f2 = len1 // length, len2 // length
            return str1[:length] * f1 == str1 and str1[:length] * f2 == str2

        for length in range(min(len1, len2), 0, -1):
            if is_divosor(length):
                return str1[:length]
        return ""

