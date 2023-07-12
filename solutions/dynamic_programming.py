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
        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
