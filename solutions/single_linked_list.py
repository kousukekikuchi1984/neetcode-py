from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        window = []
        cur = head
        length = 0
        while cur:
            length += 1
            window.append(cur)
            if len(window) == n + 1 + 1:
                del window[0]
            cur = cur.next

        if len(window) == n + 1:
            if len(window) <= 2:
                window[0].next = None
            else:
                window[0].next = window[2]
        elif len(window) == n:
            if n == 1:
                head = None
            else:
                head = window[1]
        else:
            assert False, "*** unreachable"
        return head
