class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _invert_tree(root: Optional[TreeNode]):
            if root is None:
                return
            root.left, root.right = root.right, root.left
            _invert_tree(root.left)
            _invert_tree(root.right)

        _invert_tree(root)
        return root
        
     def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _max_depth(root: Optional[TreeNode], val: int) -> int:
            if root is None:
                return val
            left = _max_depth(root.left, val + 1)
            right = _max_depth(root.right, val + 1)
            return max([left, right])

        return _max_depth(root, 0)
