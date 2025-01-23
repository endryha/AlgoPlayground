from linkedlist import create_linkedlist, print_linkedlist, ListNode


def find_midpoint_naive(head: ListNode) -> ListNode:
    current = head
    length = 0
    while current:
        length += 1
        current = current.next

    midpoint = int(length / 2)
    counter = 0
    current = head
    while current:
        if counter == midpoint:
            return current
        else:
            current = current.next
        counter += 1


def find_midpoint_2_pointers(head: ListNode) -> ListNode:
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def test_find_midpoint(head: ListNode):
    print_linkedlist(head)
    print()
    print("Solution naive")
    print("Midpoint:", find_midpoint_naive(head))
    print()
    print("Solution 2 pointers")
    print("Midpoint:", find_midpoint_2_pointers(head))


head = create_linkedlist(9)
print("Test odd list:")
test_find_midpoint(head)

print()

print("Test even list:")
head = create_linkedlist(8)
test_find_midpoint(head)
