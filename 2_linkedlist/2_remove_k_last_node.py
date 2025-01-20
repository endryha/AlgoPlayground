from linkedlist import create_linkedlist, ListNode, print_linkedlist


def remove_k_last_node_naive(head: ListNode, k: int) -> ListNode:
    print(f"[remove_k_last_node_naive] remove {k} last node in a list:")
    print_linkedlist(head)

    if k < 1:
        return head

    current = head
    size = 0
    while current:
        size += 1
        current = current.next

    if k > size:
        return head

    node_idx_to_remove = size - k - 1

    print(f"[remove_k_last_node_naive] size: {size}, node index to remove: {node_idx_to_remove}")

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


def remove_k_last_node_2_pointers(head: ListNode, k: int) -> ListNode:
    print(f"[remove_k_last_node_2_pointers] remove {k} last node in a list:")
    print_linkedlist(head)

    counter = k

    leader = ListNode(-1, head)
    while leader and counter > 0:
        counter -= 1
        leader = leader.next

    if not leader:
        return head

    follower_handler_node = ListNode(-1, head)
    follower = follower_handler_node
    while True:
        if leader.next is None:
            node_to_remove = follower.next
            follower.next = node_to_remove.next
            node_to_remove.next = None
            break

        leader = leader.next
        follower = follower.next

    return follower_handler_node.next


print("Naive")
head = create_linkedlist(10)

new_head = remove_k_last_node_naive(head, 9)

print_linkedlist(new_head)

print()
print("2 Pointers")
head = create_linkedlist(10)

new_head = remove_k_last_node_2_pointers(head, 1)

print_linkedlist(new_head)
