class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def print_linkedlist(head: ListNode) -> None:
    current = head
    while current:
        print(current.value, end=" → " if current.next else "")
        current = current.next
    print()


def create_linkedlist(size: int):
    head = ListNode(0)
    current = head
    for i in range(1, size):
        current.next = ListNode(i)
        current = current.next

    return head
