class ListNode:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        if self.next:
            return f"{self.value} → next({self.next.value})"
        else:
            return f"{self.value}"


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None

    def __str__(self):
        return f"{self.value}"


def linkedlist_str(head, prefix: str = "", suffix: str = "", formatter=None) -> str:
    current = head
    output = prefix

    if formatter is None:
        def formatter(node):
            if hasattr(node, 'key'):
                return f"({node.key},{node.value})"
            return str(node.value)

    while current:
        output += formatter(current)
        if current.next:
            output += " → "
        current = current.next

    output += suffix
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
