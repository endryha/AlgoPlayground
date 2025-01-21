from typing import Optional

from linkedlist import ListNode, create_linkedlist, get_tail_node, print_linkedlist, linkedlist_str


def find_intersection_node_hash(head1: ListNode, head2: ListNode) -> Optional[ListNode]:
    visited_nodes = set()

    current = head1
    while current:
        visited_nodes.add(current)
        current = current.next

    current = head2
    while current:
        if current in visited_nodes:
            return current

        current = current.next

    return None


def find_intersection_node_2_pointers(head1: ListNode, head2: ListNode) -> Optional[ListNode]:
    current1 = head1
    current2 = head2

    while not (current1.next is None and current2.next is None):
        if current1 == current2:
            return current1

        if current1.next is None:
            current1 = head2
        else:
            current1 = current1.next

        if current2.next is None:
            current2 = head1
        else:
            current2 = current2.next


list1 = create_linkedlist(start=0, size=5)
list2 = create_linkedlist(start=2, size=3)
tail = create_linkedlist(start=5, size=2)

tail_str = linkedlist_str(tail)
print("List 1:")
print_linkedlist(list1, suffix=" → tail(" + tail_str + ")")
print("List 2:")
print_linkedlist(list2, suffix=" → tail(" + tail_str + ")")

get_tail_node(list1).next = tail
get_tail_node(list2).next = tail

intersection_node = find_intersection_node_hash(list1, list2)

print("Intersection node (hash solution):")
print(intersection_node)

print("Intersection node (2 pointers solution):")
intersection_node = find_intersection_node_2_pointers(list1, list2)
print(intersection_node)
