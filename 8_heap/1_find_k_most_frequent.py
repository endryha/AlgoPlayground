import heapq
import unittest
from collections import Counter
from typing import List
from unittest import TestCase

from faker.proxy import Faker


class Heap:
    def __init__(self, values=None, min_heap=True):
        """
        Initialize a new heap.

        :param values: An optional list of initial values to build the heap from.
        :param min_heap: If True, the heap is a min-heap; if False, it is a max-heap.
        """
        self.min_heap = min_heap
        if values is not None:
            # Make a copy of the input list to avoid modifying it.
            self.heap = list(values)
            # Rearrange the list into a valid heap.
            self.heapify()
        else:
            self.heap = []

    def _compare(self, a, b):
        """
        Compare two values based on the type of heap.

        For a min-heap, return True if a < b.
        For a max-heap, return True if a > b.
        """
        return a < b if self.min_heap else a > b

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def heapify(self):
        """
        Rearrange the current list into a valid heap.
        This operation runs in O(n) time.
        """
        n = len(self.heap)
        # Start from the last non-leaf node and heapify downwards.
        for i in range((n // 2) - 1, -1, -1):
            self._heapify_down(i)

    def insert(self, key):
        """
        Insert a new key into the heap.
        """
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """
        Move the element at index up to its correct position to maintain the heap property.
        """
        while index > 0:
            parent_index = self.parent(index)
            if self._compare(self.heap[index], self.heap[parent_index]):
                # Swap if the child has higher priority (based on comparator).
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def pop(self):
        """
        Remove and return the root element (min for min-heap, max for max-heap).
        """
        if not self.heap:
            raise IndexError("pop from an empty heap")

        # Save the root element to return.
        root = self.heap[0]

        # Replace the root with the last element.
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        """
        Move the element at index down to its correct position to maintain the heap property.
        """
        size = len(self.heap)
        while True:
            left = self.left_child(index)
            right = self.right_child(index)
            candidate = index

            if left < size and self._compare(self.heap[left], self.heap[candidate]):
                candidate = left
            if right < size and self._compare(self.heap[right], self.heap[candidate]):
                candidate = right

            if candidate == index:
                break

            self.heap[index], self.heap[candidate] = self.heap[candidate], self.heap[index]
            index = candidate

    def peek(self):
        """
        Return the root element without removing it.
        """
        if not self.heap:
            raise IndexError("peek from an empty heap")
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)


class Pair:
    def __init__(self, string: str, freq: int, reverse_sort: bool = False):
        self.string = string
        self.freq = freq
        self.reverse_sort = reverse_sort

    def __lt__(self, other):
        if self.reverse_sort:
            if self.freq == other.freq:
                return self.string > other.string
            else:
                return self.freq < other.freq
        else:
            if self.freq == other.freq:
                return self.string < other.string
            else:
                return self.freq > other.freq

    def __str__(self):
        return f"{self.string}: {self.freq}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.string == other.string and self.freq == other.freq


def k_most_frequent_strings_max_heap(strs: List[str], k: int):
    frequencies = Counter(strs)
    max_heap = [Pair(string, freq) for string, freq in frequencies.items()]
    heapq.heapify(max_heap)
    return [heapq.heappop(max_heap) for _ in range(k)]


def k_most_frequent_strings_min_heap(strs: List[str], k: int):
    frequencies = Counter(strs)
    min_heap = []

    for s, freq in frequencies.items():
        heapq.heappush(min_heap, Pair(s, freq, True))

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    result = [heapq.heappop(min_heap) for _ in range(k)]
    result.reverse()

    return result


def k_most_frequent_strings_max_heap_custom(strs: List[str], k: int):
    frequencies = Counter(strs)

    heap = Heap(min_heap=True)
    for s, freq in frequencies.items():
        heap.insert(Pair(s, freq, True))

        if len(heap) > k:
            heap.pop()

    result = [heap.pop() for _ in range(k)]
    result.reverse()

    return result


class Test(TestCase):
    def test_k_most_frequent_strings_min_heap(self):
        fake = Faker()

        strs = []
        for _ in range(1000):
            strs.append(fake.country())

        most_frequent1 = k_most_frequent_strings_max_heap(strs, 5)
        most_frequent2 = k_most_frequent_strings_min_heap(strs, 5)
        most_frequent3 = k_most_frequent_strings_max_heap_custom(strs, 5)
        print(most_frequent1)
        print(most_frequent2)
        print(most_frequent3)

        self.assertEqual(most_frequent1, most_frequent2)
        self.assertEqual(most_frequent2, most_frequent3)

    def test_custom_heap(self):
        # Using the heap as a min-heap (default)
        print("Min-Heap Example:")
        min_heap = Heap(min_heap=True)
        for value in [5, 3, 8, 1, 2]:
            min_heap.insert(value)
            print("Heap:", min_heap)

        while min_heap.heap:
            print("Extracted:", min_heap.pop())

        print("\nMax-Heap Example:")
        # Using the heap as a max-heap
        max_heap = Heap(min_heap=False)
        for value in [5, 3, 8, 1, 2]:
            max_heap.insert(value)
            print("Heap:", max_heap)

        while max_heap.heap:
            print("Extracted:", max_heap.pop())


if __name__ == "__main__":
    unittest.main()
