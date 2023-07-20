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
        available_triplets = []
        for i in range(len(triplets)):
            if all([ triplets[i][j] <= target[j]  for j in range(len(triplets[i]))]):
                available_triplets.append(triplets[i])
        if not available_triplets:
            return False
        for i, row in enumerate(zip(*available_triplets)):
            if max(row) != target[i]:
                return False
        return True
