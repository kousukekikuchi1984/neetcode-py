class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if nums[i] + i + 1 > target:
                target = i
        return target == 0

    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        res = 0
        while right < len(nums) - 1:
            max_jump = 0
            for i in range(left, right + 1):
                max_jump = max(max_jump, i + nums[i])
            left = right + 1
            right = max_jump
            res += 1
        return res
