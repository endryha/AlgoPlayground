import heapq
import unittest
from unittest import TestCase


class MedianOfIntStream:
    def __init__(self):
        self.left_half = []
        self.right_half = []

    def add(self, num: int):
        print("add →", num)
        if len(self.left_half) == 0 or num <= -self.left_half[0]:
            heapq.heappush(self.left_half, -num)
        else:
            heapq.heappush(self.right_half, num)

        if len(self.left_half) > len(self.right_half) + 1:
            heapq.heappush(self.right_half, -heapq.heappop(self.left_half))
        elif len(self.left_half) < len(self.right_half):
            heapq.heappush(self.left_half, -heapq.heappop(self.right_half))

        print("left:", self.left_half, "right:", self.right_half)

    def get_median(self) -> int:
        if len(self.left_half) == 0:
            return 0

        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2
        else:
            return -self.left_half[0]


class Test(TestCase):

    def test_median_of_int_stream(self):
        stream = MedianOfIntStream()

        nums = [10, 2, 8, 4, 11, 3, 7, 20, 9, 5]

        for num in nums:
            stream.add(num)
            print("median →", stream.get_median())


if __name__ == "__main__":
    unittest.main()
