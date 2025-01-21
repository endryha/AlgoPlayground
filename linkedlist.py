class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        if self.next:
            return f"{self.value} → next({self.next.value})"
        else:
            return f"{self.value}"


def linkedlist_str(head: ListNode, prefix: str = "", suffix: str = "") -> str:
    current = head
    output = prefix if prefix else ""

    while current:
        output += str(current.value)
        if current.next:
            output += " → "
        current = current.next

    output += suffix if suffix else ""
    return output


def print_linkedlist(head: ListNode, prefix: str = "", suffix: str = "") -> None:
    print(linkedlist_str(head, prefix, suffix))


def create_linkedlist(size: int, start: int = None):
    head = ListNode(start)
    current = head
    for i in range(start + 1, start + size):
        current.next = ListNode(i)
        current = current.next

    return head


def get_tail_node(start_node: ListNode):
    current = start_node
    while current.next:
        current = current.next

    return current
