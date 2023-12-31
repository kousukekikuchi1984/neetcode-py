from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        dp[0] = cost[0]; dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[len(cost) - 1], dp[len(cost) - 2])

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]; dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[:i - 1]) + nums[i]
        return max(dp[-1], dp[-2])

    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)

    def maxProduct(self, nums: List[int]) -> int:
        cur_min = cur_max = 1
        res = nums[0]
        for n in nums:
            if n == 0:
                cur_min = cur_max = 1
                continue
            multiply_to_max = cur_max * n
            multiply_to_min = cur_min * n
            cur_min = min(multiply_to_max, multiply_to_min, n)
            cur_max = max(multiply_to_max, multiply_to_min, n)
            res = max(res, cur_max)
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_length = len(s)
        dp = [False] * (s_length + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= s_length and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # (i, for_buy) -> max profit

        def dfs(i: int, for_buy: bool) -> int:
            if i >= len(prices):
                return 0
            if dp.get((i, for_buy)):
                return dp[(i, for_buy)]

            # cooldown does nothing.
            cooldown = dfs(i + 1, for_buy)
            if for_buy:
                buy = dfs(i + 1, not for_buy) - prices[i]
                dp[(i, for_buy)] = max(cooldown, buy)
            else:
                sell = dfs(i + 2, not for_buy) + prices[i]
                dp[(i, for_buy)] = max(cooldown, sell)
            return dp[(i, for_buy)]

        return dfs(0, True)

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}  # (i, j): longest increasing path

        def dfs(i: int, j: int, move_from: int) -> int:
            if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[0]):
                return 0
            if matrix[i][j] <= move_from:
                return 0
            if dp.get((i, j)):
                return dp[i, j]

            can_move_to = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            values = []
            for di, dj in can_move_to:
                val = dfs(i + di, j + dj, matrix[i][j])
                values.append(val)
            current = max(values) + 1
            dp[(i, j)] = current
            return current

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, 0)
        return max(dp.values())

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}  # (L, R): val

        def dfs(left: int, right: int) -> int:
            # ここだけ
            if left > right:
                return 0
            if dp.get((left, right)):
                return dp[(left, right)]
            total_coins = []
            for partition in range(left, right + 1):
                current = nums[left - 1] * nums[partition] * nums[right + 1]
                total = dfs(left, partition - 1) + current + dfs(partition + 1, right)
                total_coins.append(total)
            max_coins = max(total_coins)
            dp[(left, right)] = max_coins
            return max_coins

        return dfs(1, len(nums) - 2)

    def isMatch(self, s: str, p: str) -> bool:
        # dp: columns: p + 1, index 0 means empty string
        #     rows: s + 1, index 0 means empty string
        #     dp[n][0] == True means starting points.

        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True

        # regex "*" can be a starting point when ignore former letter
        for row in range(2, len(p) + 1):
            if p[row - 1] == "*":
                dp[row][0] = dp[row - 2][0]

        for row in range(1, len(p) + 1):
            for column in range(1, len(s) + 1):
                former_state = dp[row - 1][column - 1]
                current_regex = p[row - 1]
                if s[column - 1] == current_regex or current_regex == ".":
                    dp[row][column] = former_state
                elif p[row - 1] == "*":
                    # ignore former regex -> use the value at row - 2
                    # if regex is matched -> ignore case or former column
                    dp[row][column] = dp[row - 2][column]
                    if p[row - 2] == "." or p[row - 2] == s[column - 1]:
                        dp[row][column] |= dp[row][column - 1]
        return dp[len(p)][len(s)]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for row in range(len(triangle) - 2, -1, -1):
            for column in range(len(triangle[row])):
                dp[column] = min(dp[column], dp[column + 1]) + triangle[row][column]
        return dp[0]

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n in (1, 2):
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]

    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            cur = nums[i] * count[nums[i]]
            if i > 0 and nums[i] == nums[i - 1] + 1:
                tmp = earn2
                earn2 = max(cur + earn1, earn2)
                earn1 = tmp
            else:
                tmp = earn2
                earn2 = cur + earn2
                earn1 = tmp
        return earn2

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        nums.sort()
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                dp[i] = dp[i - num]
        return dp[target]

    def numSquares(self, n: int) -> int:
        dp = list(range(n + 1))  # 1
        max_num = int(n ** 0.5)
        for num in range(2, max_num + 1):
            val = num ** 2
            for i in range(0, n + 1):
                if i + val < n:
                    dp[i + val] = min(dp[i] + val, dp[i + val])
                else:
                    break
        return dp[-1]

    def integerBreak(self, n: int) -> int:
        dp = {1: 1}
        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num], val)
        return dp[n]

    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}  # key = index, value = [length of LIS, count]
        lenLIS, res = 0, 0  # length of LIS, count of LIS

        # i = start of subseq
        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCnt = 1, 1  # len, cnt of LIS start from i

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]  # len, cnt of LIS start from j
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            dp[i] = [maxLen, maxCnt]

        return res

    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def rob2(self, nums: List[int]) -> int:
        def helper(nums: List[int]) -> int:
            if len(nums) < 2:
                return max(nums)
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = nums[1]
            for i in range(2, len(nums)):
                dp[i] = max(dp[:i-1]) + nums[i]
            return max(dp)

        if len(nums) < 2:
            return max(nums)
        return max(helper(nums[1:]), helper(nums[:-1]))

    def longestPalindrome(self, s: str) -> str:
        chars = ""
        length = 0
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    # palindromic
                    tmp = s[left:right + 1]
                    tmp_length = len(tmp)
                    if tmp_length > length:
                        length = tmp_length
                        chars = tmp
                    left -= 1
                    right += 1
                else:
                    break

        for i in range(len(s)):
            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    tmp = s[left:right + 1]
                    tmp_length = len(tmp)
                    if tmp_length > length:
                        length = tmp_length
                        chars = tmp
                    left -= 1
                    right += 1
                else:
                    break
        return chars

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != float("inf"):
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[amount] if dp[amount] != float("inf") else -1

    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        chars = set(s)
        for char in chars:
            first, last = s.find(char), s.rfind(char)
            count += len(set(s[first + 1: last]))
        return count

    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = {(1,1): 1}
        for N in range(2, n + 1):
            for K in range(1, k + 1):
                dp[(N, K)] = dp.get((N - 1, K - 1), 0) + (N - 1) * dp.get((N - 1, K), 0)
        return dp[(n, k)] % (10 ** 9 + 7)

    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(left: int, right: int) -> int:
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]

            even = True if (right - left) % 2 else False
            left_value = piles[left] if even else 0
            right_value = piles[right] if even else 0

            dp[(left, right)] = max(dfs(left + 1, right) + left_value, dfs(left, right - 1) + right_value)
            return dp[(left, right)]
        
        return dfs(0, len(piles) - 1) > sum(piles) // 2

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        window = deque([0])

        for i in range(1, len(s)):
            if window and window[0] + maxJump < i:
                window.popleft()
            if s[i] == "0" and window and window[0] + minJump <= i:
                window.append(i)
        return window and window[-1] == len(s) - 1

    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}

        def dfs(left: int, right: int) -> int:
            if right - left == 1:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]

            result = float("inf")
            for cur in cuts:
                if left < cut < right:
                    result = min(
                        result,
                        (right - left) + dfs(left, cur) + dfs(cur, right),
                    )
            dp[(left, right)] = result = 0 if result == float("inf") else result
            return result

        return dfs(0, n)
