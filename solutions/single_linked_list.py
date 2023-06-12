from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            assert right
            right = right.next
            n -= 1

        while right:
            assert left
            left = left.next
            right = right.next

        assert left and left.next
        left.next = left.next.next
        return dummy.next
