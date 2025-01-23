from linkedlist import create_linkedlist, print_linkedlist, get_tail_node, ListNode


def is_cycled_hashset(head: ListNode) -> bool:
    visited_nodes = set()
    current = head
    while current:
        if current in visited_nodes:
            print(f"visited({current.value}) -> True")
            return True

        print(f"visited({current.value}) -> False")
        visited_nodes.add(current)
        current = current.next

    return False


def is_cycled_2_pointers(head: ListNode) -> bool:
    fast = head.next
    slow = head
    while fast and slow:
        if fast == slow:
            print(f"slow({slow.value})==fast({fast.value})")
            return True
        else:
            print(f"slow({slow.value})<>fast({fast.value})")

        if fast.next is None:
            return False
        else:
            fast = fast.next.next

        slow = slow.next
    return False


head1 = create_linkedlist(start=0, size=4)
head2 = create_linkedlist(start=4, size=3)
head3 = create_linkedlist(start=0, size=10)

cycled_tail = create_linkedlist(start=7, size=3)
get_tail_node(cycled_tail).next = cycled_tail

get_tail_node(head1).next = cycled_tail
get_tail_node(head2).next = cycled_tail

print("Cycled tail:")
print_linkedlist(cycled_tail)
print("List 1")
print_linkedlist(head1)
print("List 2")
print_linkedlist(head2)

print()
print("Hashset Solution")
print("List 1, is cycled =", is_cycled_hashset(head1))
print("List 2, is cycled =", is_cycled_hashset(head2))
print("List 3, is cycled =", is_cycled_hashset(head3))

print()
print("2 Pointers Solution")
print("List 1, is cycled =", is_cycled_2_pointers(head1))
print("List 2, is cycled =", is_cycled_2_pointers(head2))
print("List 3, is cycled =", is_cycled_2_pointers(head3))
