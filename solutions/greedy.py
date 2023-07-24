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

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        idx = 0
        gas_remaining = 0
        for i in range(len(gas)):
            gas_remaining += gas[i] - cost[i]
            if gas_remaining < 0:
                gas_remaining = 0
                idx = i + 1
        return idx

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hands = {}
        for val in hand:
            if val in hands:
                hands[val] += 1
            else:
                hands[val] = 1

        heap = heapq(hands.keys())
        heapq.heapify(heap)
        while heap:
            first = heap[0]

            for i in range(first, first + groupSize):
                if i not in hands:
                    return False
                hands[i] -= 1
                if hands[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current = [False, False, False]

        for triplet in triplets:
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue
            for i in range(3):
                if triplet[i] == target[i]:
                    current[i] = True
        return all(current)

    def partitionLabels(self, s: str) -> List[int]:
        words = {}  # char, [start, end]
        for i, c in enumerate(s):
            if c in words:
                words[c][1] = i
            else:
                words[c] = [i, i]

        results = []
        start = end = 0
        is_first = True
        for r in words.values():
            if is_first:
                start, end = r[0], r[1]
                is_first = False
                continue
            if start < r[0] < end:
                if r[1] > end:
                    end = r[1]
            elif end < r[0]:
                results.append(end - start + 1)
                start, end = r[0], r[1]
        results.append(end - start + 1)
        return results

    def checkValidString(self, s: str) -> bool:
        left_min = left_max = 0
        for c in s:
            if c == "(":
                left_min += 1
                left_max += 1
            elif c == ")":
                left_min -= 1
                left_max -= 1
            elif c == "*":
                left_min -= 1
                left_max += 1
            else:
                assert False, f"*** unexpected character: {c}"
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0
        return left_min == 0
