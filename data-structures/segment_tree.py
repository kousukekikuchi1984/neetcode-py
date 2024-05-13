from typing import Optional

class Tree:
    total: int
    left: Optional["Tree"]
    right: Optional["Tree"]
    ridx: int
    lidx: int

    def __init__(self, total: int, lidx: int, ridx: int):
        self.total = total
        self.ridx = ridx
        self.lidx = lidx
        self.left = None
        self.right = None


class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self._build_tree(nums, 0, len(nums) - 1)

    def _build_tree(self, nums: List[int], lidx: int, ridx: int):
        if lidx == ridx:
            return Tree(nums[lidx], lidx, ridx)
        #
        mid = (lidx + ridx) // 2
        node = Tree(0, lidx, ridx)
        node.left = self._build_tree(nums, lidx, mid)
        node.right = self._build_tree(nums, mid + 1, ridx)
        node.total = node.left.total + node.right.total
        return node
    
    def update(self, index: int, val: int) -> None:
        self._update(self.root, index, val)

    def _update(self, node: Tree, index: int, val: int):
        if node.lidx == node.ridx:
            node.total = val
            return
        mid = (node.lidx + node.ridx) // 2
        if index > mid:
            self._update(node.right, index, val)
        else:
            self._update(node.left, index, val)
        node.total = node.left.total + node.right.total
    
    def query(self, L: int, R: int) -> int:
        return self._query(self.root, L, R)

    def _query(self, node: Tree, L: int, R: int):
        if L <= node.lidx and R >= node.ridx:
            return node.total
        #
        if R < node.lidx or L > node.ridx:
            return 0
        #
        return self._query(node.left, L, R) + self._query(node.right, L, R)
