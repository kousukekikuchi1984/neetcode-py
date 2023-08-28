class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def is_valid(threshold: int):
            i, count = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= threshold:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == p:
                    return True
            return False

        if p == 0:
            return 0
        nums.sort()
        left, right = 0, 10**9
        res = 10**9

        while left <= right:
            mid = left + (right - left) // 2
            if is_valid(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
