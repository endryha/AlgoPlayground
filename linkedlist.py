from typing import Any, Optional, Callable


class ListNode:
    def __init__(self, value: Any = None, next_node: Optional['ListNode'] = None) -> None:
        self.value = value
        self.next = next_node

    def __str__(self) -> str:
        if self.next:
            return f"{self.value} → next({self.next.value})"
        return str(self.value)

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other):
        return self.value < other.value


class DoublyLinkedListNode:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value
        self.next: Optional['DoublyLinkedListNode'] = None
        self.prev: Optional['DoublyLinkedListNode'] = None

    def __str__(self) -> str:
        if self.next:
            return f"({self.key},{self.value}) → next({self.next.key},{self.next.value})"
        return f"({self.key},{self.value})"

    def __repr__(self) -> str:
        return self.__str__()


def linkedlist_str(
        head: ListNode,
        prefix: str = "",
        suffix: str = "",
        formatter: Optional[Callable[[Any], str]] = None,
) -> str:
    if formatter is None:
        def formatter(node: Any) -> str:
            if hasattr(node, 'key'):
                if node.value:
                    return f"({node.key},{node.value})"
                else:
                    return f"({node.key})"
            return str(node.value)

    visited_nodes = set()
    parts = []
    current = head
    is_cycled = False
    while current:
        parts.append(formatter(current))

        if current in visited_nodes:
            is_cycled = True
            break

        visited_nodes.add(current)

        current = current.next

    if is_cycled:
        suffix += "! (cycled)"
    return f"{prefix}{' → '.join(parts)}{suffix}"


def print_linkedlist(head: Optional[ListNode], prefix: str = "", suffix: str = "") -> None:
    print(linkedlist_str(head, prefix, suffix))


def create_linkedlist(size: int, start: int = 0) -> ListNode:
    head = ListNode(start)
    current = head
    for i in range(start + 1, start + size):
        current.next = ListNode(i)
        current = current.next
    return head


def get_tail_node(start_node: Optional[ListNode]) -> Optional[ListNode]:
    current = start_node
    while current and current.next:
        current = current.next
    return current
