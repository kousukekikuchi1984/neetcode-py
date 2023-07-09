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
        if s[0] == "0":
            return 0
        max_idx = len(s) - 1
        res = 1
        trans_1 = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        trans_2 = set(["1", "2", "3", "4", "5", "6"])
        for i in range(len(s)):
            c = s[i]
            match c:
                case "1" | "2":
                    # we must check next value
                    # 1 -> 1-9 then increment res
                    # 2 -> 1-6 then increment res
                    next_id = i + 1
                    if next_id <= max_idx and ((c == "1" and s[next_id] in trans_1) or (c == "2" and s[next_id] in trans_2)):
                        res += 1
                case _:
                    continue
        return res
