from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._sort(pairs, 0, len(pairs) - 1)
        return pairs

    def _sort(self, pairs: List[Pair], start: int, end: int):
        if end <= start:
            return

        pivot = pairs[end]
        left = start

        for i in range(start, end):
            if pairs[i].key < pivot.key:
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1

        pairs[end], pairs[left] = pairs[left], pivot
        self._sort(pairs, start, left - 1)
        self._sort(pairs, left + 1, end)
