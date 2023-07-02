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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def _max_depth(root: Optional[TreeNode]) -> int:
            nonlocal result

            if root is None:
                return 0
            left = _max_depth(root.left)
            right = _max_depth(root.right)
            result = max(result, left + right)
            return 1 + max(left, right)

        _max_depth(root)
        return result

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def _max_depth(root: Optional[TreeNode], depth: int) -> Tuple[bool, int]:
            if root is None:
                return  [True, 1]

            left = _max_depth(root.left, depth + 1)
            right = _max_depth(root.right, depth + 1)
            balanced = left[0] and right[0] and abs(right[1] - left[1]) <= 1
            return balanced, max(right[1], left[1])
        
        return _max_depth(root, 0)[0]

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def _dfs(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False

            if p.val != q.val:
                return False

            left  = _dfs(p.left, q.left)
            right = _dfs(p.right, q.right)
            return left and right
        return _dfs(p, q)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        candidates = []
        def _find_subroot_top(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if root is None:
                return False
            # root and subroot is [1, 2000) 
            if root.val == subRoot.val:
                candidates.append(root)
                return True
            return _find_subroot_top(root.left, subRoot) or _find_subroot_top(root.right, subRoot)

        def _check_subroot(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot:
                return True
            if (not root and subRoot) or (root and not subRoot):
                return False
            if root != subRoot:
                return False
            return _check_subroot(root.left, subRoot.left) and _check_subroot(root.right, subRoot.right)

        _find_subroot_top(root, subRoot)
        for node in candidates:
            if _check_subroot(node, subRoot):
                return True
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        assert False, "`p` and `q` will exist in the BST"

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], maxval = int) -> int:
            if node is None:
                return 0
           
            cnt = int(node.val >= maxval)
            maxval = max(maxval, node.val)
            left = dfs(node.left, maxval)
            right = dfs(node.right, maxval)
            return left + right + cnt
        return dfs(root, root.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(root: Optional[TreeNode], left: int, right: int) -> bool:
            if root is None:
                return True
            if not (left < root.val < right):
                return False

            return is_valid(root.left, left, root.val) and is_valid(root.right, root.val, right)
        return is_valid(root, float("-inf"), float("inf"))

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -1001
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal result
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)
            current_max = max(root.val, root.val + left, root.val + right, root.val + left + right)
            result = max(result, current_max)
            return root.val + max(left, right)

        dfs(root)
        return result


class Codec:

    def serialize(self, root: TreeNode):
        vals = []
        def dfs(root: Optional[TreeNode]):
            if root is None:
                vals.append("N")
                return
            vals.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(vals)
        

    def deserialize(self, data: str):
        vals = data.split(",")

        def dfs() -> Optional[TreeNode]:
            val = vals.pop(0)
            if val == "N":
                return None
            node = TreeNode(val=int(val)) 
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
