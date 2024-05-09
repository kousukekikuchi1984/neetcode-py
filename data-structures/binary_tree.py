from typing import Optional, List


class TreeNode:
    key: int
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    root: Optional[TreeNode]

    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int):
        node = self.root
        new = TreeNode(key, val)
        if self.root is None:
            self.root = new
            return
        while True:
            if key < node.key:
                if node.left == None:
                    node.left = new
                    return
                node = node.left
            elif key > node.key:
                if node.right == None:
                    node.right = new
                    return
                node = node.right
            else:
                node.val = val
                return

    def get(self, key: int) -> int:
        node = self.root
        while True:
            if node is None:
                return -1
            elif key == node.key:
                return node.val
            elif key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left
            else:
                assert False, "*** unreachable"

    def getMin(self) -> int:
        if self.root is None:
            return -1
        node = self.root
        while True:
            if node.left:
                node = node.left
            else:
                return node.val

    def getMax(self) -> int:
        if self.root is None:
            return -1
        node = self.root
        while True:
            if node.right:
                node = node.right
            else:
                return node.val

    def remove(self, key: int):
        parent = None
        node = self.root
        while node is not None:
            if key < node.key:
                parent = node
                node = node.left
            elif key > node.key:
                parent = node
                node = node.right
            else:
                if node.left and node.right:
                    min_larger_node = node.right
                    min_larger_parent = node
                    while min_larger_node.left:
                        min_larger_parent = min_larger_node
                        min_larger_node = min_larger_node.left
                    node.key = min_larger_node.key
                    node.val = min_larger_node.val
                    if min_larger_parent.left == min_larger_node:
                        min_larger_parent.left = min_larger_node.right
                    else:
                        min_larger_parent.right = min_larger_node.right
                elif node.left or node.right:
                    child = node.left if node.left else node.right
                    if node == self.root:
                        self.root = child
                    elif parent.left == node:
                        parent.left = child
                    else:
                        parent.right = child
                else:
                    if node == self.root:
                        self.root = None
                    elif parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                return
            if node is None:
                return

    def getInorderKeys(self) -> List[int]:
        results = []
        def _get_inorder_keys(node: TreeNode):
            if node:
                _get_inorder_keys(node.left)
                results.append(node.key)
                _get_inorder_keys(node.right)
        #
        _get_inorder_keys(self.root)
        return results
