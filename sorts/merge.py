class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.sort(pairs, 0, len(pairs) - 1)
        return pairs

    def sort(self, pairs: List[Pair], left: int, right: int):
        if left < right:
            mid = (left + right) // 2
            self.sort(pairs, left, mid)
            self.sort(pairs, mid + 1, right)
            self.merge(pairs, left, mid, right)

    def merge(self, pairs: List[Pair], left: int, mid: int, right: int):
        L = pairs[left:mid+1]
        R = pairs[mid+1:right+1]
        lpoint = rpoint = 0
        cur = left
        while lpoint < len(L) and rpoint < len(R):
            lval = L[lpoint]
            rval = R[rpoint]
            if lval.key <= rval.key:
                pairs[cur] = L[lpoint]
                lpoint += 1
            else:
                pairs[cur] = R[rpoint]
                rpoint += 1
            cur += 1

        while lpoint < len(L):
            pairs[cur] = L[lpoint]
            lpoint += 1
            cur += 1

        while rpoint < len(R):
            pairs[cur] = R[rpoint]
            rpoint += 1
            cur += 1
