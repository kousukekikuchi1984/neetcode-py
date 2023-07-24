class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None
        copy = {}
        cur = head
        while cur:
            copy[cur] = Node(x=cur.val, next=cur.next, random=cur.random)
            cur = cur.next

        dummy = Node(x=0, next=head)
        cur = dummy
        while cur:
            cur.next = copy.get(cur.next)
            cur.random = copy.get(cur.random)
            cur = cur.next

        return copy[head]
