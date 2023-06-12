from solutions.single_linked_list import ListNode, Solution


class TestSolution:
    def test_removeNthFromEnd(self):
        head = ListNode(
            val=1,
            next=ListNode(
                val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))
            ),
        )
        solution = Solution()
        actual = solution.removeNthFromEnd(head, 2)
        actual_lis = []
        a = actual
        while a:
            actual_lis.append(a.val)
            a = a.next
        expected_lis = [1, 2, 3, 5]
        assert actual_lis == expected_lis
