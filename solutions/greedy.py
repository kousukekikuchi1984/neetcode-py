class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if nums[i] + i + 1 > target:
                target = i
        return target == 0
