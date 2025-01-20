from typing import Optional

from linkedlist import create_linkedlist, print_linkedlist, ListNode


def linkedlist_reversal(head: ListNode) -> ListNode:
    current = head
    previous = None

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


def linkedlist_reversal_recursive(current: ListNode, prev: Optional[ListNode] = None) -> ListNode:
    if not current:
        return prev

    next = current.next
    current.next = prev

    return linkedlist_reversal_recursive(next, current)


head = create_linkedlist(10)
print("Original linked list:")
print_linkedlist(head)

print("Reversed linked list:")
print_linkedlist(linkedlist_reversal(head))

print()

head = create_linkedlist(10)
print("Original linked list:")
print_linkedlist(head)

print("Reversed linked list:")
print_linkedlist(linkedlist_reversal_recursive(head))
