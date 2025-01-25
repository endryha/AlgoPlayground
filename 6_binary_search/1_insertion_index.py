import unittest
from typing import List
from unittest import TestCase


def find_insertion_index(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    mid = (left + right) // 2

    while left < right:
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

        mid = (left + right) // 2

    return left


class Test(TestCase):
    def test_find_insertion_index(self):
        nums = [1, 2, 3, 4, 6, 7, 8, 9]
        target = 4

        print("input:", nums)
        print("target:", target)

        index = find_insertion_index(nums, target)

        print("index:", index)

        self.assertEqual(3, index)


if __name__ == '__main__':
    unittest.main()
