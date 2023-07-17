class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if nums[i] + i + 1 > target:
                target = i
        return target == 0

    def jump(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i: int, path) -> int:
            if nums[i] == 0:
                return 1111111
            if i == len(nums) - 1:
                return path
            if i + nums[i] + 1 >= len(nums):
                return path + 1
            return min([dfs(i + j, path + 1) for j in range(1, nums[i] + 1)])

        if nums[0] == 0:
            return 0
        return dfs(0, 0)
