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

    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        finds = None
        while left <= right:
            center = (left + right) // 2
            if nums[center] < target:
                left = center + 1
            elif nums[center] == target:
                finds = center
                break
            elif nums[center] > target:
                right = center - 1
            else:
                assert False, "*** unreachable"
        #
        if finds is None:
            return [-1, -1]
        left = right = finds
        while left > 0 and nums[left - 1] == target:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] == target:
            right += 1
        return [left, right]
