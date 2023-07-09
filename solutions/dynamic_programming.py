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
