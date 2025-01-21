from typing import Optional

from linkedlist import DoublyLinkedListNode, doubly_linkedlist_str


class LruCache:
    head: Optional[DoublyLinkedListNode] = None
    tail: Optional[DoublyLinkedListNode] = None

    cache = {}

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.capacity = capacity

    def get(self, key) -> Optional[DoublyLinkedListNode]:
        print(f"get({key})")
        if key in self.cache:
            node = self.cache[key]

            if key == self.head.key:
                self.remove_from_head()
            elif key != self.tail.key:
                self.remove_node(node)

            self.add_to_tail(node)

            return node.value
        else:
            return None

    def remove_node(self, node: DoublyLinkedListNode):
        del self.cache[node.key]

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        node.prev = None
        node.next = None

        if len(self.cache) == 0:
            self.head = None
            self.tail = None

    def remove_from_head(self):
        next = self.head.next
        self.remove_node(self.head)
        self.head = next

    def remove_from_tail(self):
        prev = self.tail.prev
        self.remove_node(self.tail)
        self.tail = prev

    def add_to_tail(self, node: DoublyLinkedListNode):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.cache[node.key] = node

    def put(self, key, value) -> None:
        print(f"put({key},{value})")

        # node: DoublyLinkedListNode
        if key in self.cache:
            if key == self.head.key:
                self.remove_from_head()
            elif key == self.tail.key:
                self.remove_from_tail()
            else:
                self.remove_node(self.cache[key])
        elif len(self.cache) >= self.capacity:
            self.remove_from_head()

        self.add_to_tail(DoublyLinkedListNode(key, value))

    def items(self) -> dict:
        return {key: obj.value for key, obj in self.cache.items()}

    def __len__(self):
        return len(self.cache)

    def __str__(self):
        return f"size: {len(self)}, items: {doubly_linkedlist_str(self.head)}"


lru = LruCache(4)

lru.put(1, 1)
print(lru, end="\n\n")
lru.put(2, 2)
print(lru, end="\n\n")
lru.put(3, 3)
print(lru, end="\n\n")
lru.put(3, 3)
print(lru, end="\n\n")
lru.get(1)
print(lru, end="\n\n")
lru.put(4, 4)
print(lru, end="\n\n")
lru.get(2)
print(lru, end="\n\n")
lru.get(3)
print(lru, end="\n\n")
lru.put(5, 5)
print(lru, end="\n\n")
