from solution.random_linked_list import Node, Solution


class TestSolution:

    def test_copyRandomList(self):
        node1 = Node(val=7, random=None)
        node2 = Node(val=13, random=node1)
        node1.next = node2
        node3 = Node(val=11)
        node2.next = node3
        node4 = Node(val=10, random=node3)
        node3.next = node4
        node5 = Node(val=1, random=node1)
        node4.next = node5

        solution = Solution()
        a = solution.copyRandomList(node1)
        actual = []
        while a:
            random = a.next.val if a.next else None
            actual.append(a.val, next)
            a = a.next
        expected = [(7, None), (13, 7), (11, 1), (10, 11), (1, 7)]
        assert actual == expected
