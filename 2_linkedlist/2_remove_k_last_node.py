from typing import Optional

from linkedlist import create_linkedlist, ListNode, print_linkedlist

head = create_linkedlist(10)


def remove_k_last_node_naive(head: ListNode, k: int) -> Optional[ListNode]:
    print(f"Remove {k} last node in a list:")
    print_linkedlist(head)

    if not head or k < 1:
        return None

    current = head
    size = 0
    while current:
        size += 1
        current = current.next

    if k > size:
        return head

    node_idx_to_remove = size - k - 1

    # print(f"Size: {size}, node index to remove: {node_idx_to_remove}")

    dummy_head = ListNode(None, head)
    current = dummy_head
    i = 0
    while current:
        if node_idx_to_remove + 1 == i:
            node_to_remove = current.next
            current.next = node_to_remove.next
            node_to_remove.next = None
            break
        current = current.next
        i += 1

    return dummy_head.next


# print_linkedlist(head)

new_head = remove_k_last_node_naive(head, 11)

print("List with removed node:")
print_linkedlist(new_head)
