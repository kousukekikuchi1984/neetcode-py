class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(len(nums)):
            if dp[i] and nums[i] != 0:
                for j in range(1, dp[i] + 1):
                    index = i + j
                    if index >= len(nums):
                        break
                    dp[index] = True
        return dp[len(nums) - 1]
