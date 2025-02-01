import heapq
import unittest
from typing import List
from unittest import TestCase

import linkedlist
from linkedlist import ListNode, create_linkedlist


def combine_sorted_linked_lists(lists: List[ListNode]) -> ListNode:
    heap = []

    for head in lists:
        if head:
            heapq.heappush(heap, head)

    start = ListNode()
    curr = start

    while len(heap) > 0:
        print(heap)

        node = heapq.heappop(heap)

        curr.next = node
        curr = node

        if node.next:
            heapq.heappush(heap, node.next)

    return start.next


class Test(TestCase):

    def test_combine_sorted_linked_lists(self):
        lists = [
            create_linkedlist(start=0, size=3),
            create_linkedlist(start=3, size=2),
            create_linkedlist(start=5, size=3),
            create_linkedlist(start=9, size=4)
        ]

        print(lists)

        head = combine_sorted_linked_lists(lists)

        linkedlist.print_linkedlist(head)


if __name__ == '__main__':
    unittest.main()
