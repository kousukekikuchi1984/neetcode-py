from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])

    def rob(self, nums: List[int]) -> int:
        def helper(nums: List[int]):
            rob1, rob2 = 0, 0
            for n in nums:
                new_rob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

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
