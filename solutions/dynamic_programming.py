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
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)
