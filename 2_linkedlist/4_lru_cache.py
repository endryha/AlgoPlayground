from typing import Optional

from linkedlist import DoublyLinkedListNode, linkedlist_str


class LruCache:
    head: Optional[DoublyLinkedListNode] = None
    tail: Optional[DoublyLinkedListNode] = None

    cache = {}

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.capacity = capacity

    def get(self, key):
        result = None
        if key in self.cache:
            node = self.cache[key]

            if key != self.tail.key:
                if key == self.head.key:
                    self._remove_from_head()
                else:
                    self._remove_node(node)
                self._add_to_tail(node)

            result = node.value

        print(f"get({key}) → {result}")

    def put(self, key, value) -> None:
        print(f"put({key},{value})")

        # node: DoublyLinkedListNode
        if key in self.cache:
            if key == self.head.key:
                self._remove_from_head()
            elif key == self.tail.key:
                self._remove_from_tail()
            else:
                self._remove_node(self.cache[key])
        elif len(self.cache) >= self.capacity:
            self._remove_from_head()

        self._add_to_tail(DoublyLinkedListNode(key, value))

    def _remove_node(self, node: DoublyLinkedListNode):
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

    def _remove_from_head(self):
        next = self.head.next
        self._remove_node(self.head)
        self.head = next

    def _remove_from_tail(self):
        prev = self.tail.prev
        self._remove_node(self.tail)
        self.tail = prev

    def _add_to_tail(self, node: DoublyLinkedListNode):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.cache[node.key] = node

    def items(self) -> dict:
        return {key: obj.value for key, obj in self.cache.items()}

    def __len__(self):
        return len(self.cache)

    def __str__(self):
        return f"size: {len(self)}, items: (head) → " + linkedlist_str(self.head) + " → (tail)"


class LruCacheSimplified:
    head = DoublyLinkedListNode('head', None)
    tail = DoublyLinkedListNode('tail', None)

    head.next = tail
    tail.prev = head

    cache = {}

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.capacity = capacity

    def get(self, key):
        result = None
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._add_to_tail(node)
            result = node.value

        print(f"get({key}) → {result}")

    def put(self, key, value) -> None:
        print(f"put({key},{value})")

        if key in self.cache:
            self._remove_node(self.cache[key])
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            del self.cache[self.head.next.key]
            self._remove_node(self.head.next)

        node = DoublyLinkedListNode(key, value)
        self._add_to_tail(node)
        self.cache[key] = node

    def _remove_node(self, node: DoublyLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def _add_to_tail(self, node: DoublyLinkedListNode):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def __len__(self):
        return len(self.cache)

    def __str__(self):
        return f"size: {len(self)}, items: " + linkedlist_str(self.head)


def test_lru_cache(lru) -> None:
    lru.put(1, 1)
    print(lru, end="\n\n")
    lru.put(2, 2)
    print(lru, end="\n\n")
    lru.put(3, 3)
    print(lru, end="\n\n")
    lru.put(3, 3)
    print(lru, end="\n\n")
    lru.get(10)
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
    lru.get(5)
    print(lru, end="\n\n")
    lru.get(1)
    print(lru, end="\n\n")


capacity = 4

lru = LruCache(capacity)
lru_simplified = LruCacheSimplified(capacity)

print('LruCache')
test_lru_cache(lru)
print()
print('LruCacheSimplified')
test_lru_cache(lru_simplified)
