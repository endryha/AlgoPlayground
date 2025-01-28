import unittest
from typing import List
from unittest import TestCase


def find_the_target_in_a_rotated_sorted_array(nums: List[int], target: int) -> int:
    pivot = find_pivot_in_a_rotated_sorted_array(nums)

    target_index = binary_search(nums, target, 0, pivot - 1)
    if target_index != -1:
        return target_index
    else:
        return binary_search(nums, target, pivot, len(nums) - 1)


def find_pivot_in_a_rotated_sorted_array(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[left]:
            right = mid - 1
        else:
            left = mid + 1

    return left


def binary_search(nums: List[int], target: int, left: int, right: int) -> int:
    while left <= right:
        mid = (left + right) // 2

        # print(f"left={left} mid={mid} right={right}")

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


class Test(TestCase):
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [7, 8, 9]
    rotated_array = nums2 + nums1

    def test_find_the_target_in_a_rotated_sorted_array(self):
        print("Rotated sorted array:", self.rotated_array)

        expected_indices = [3, 4, 5, 6, 7, 8, 0, 1, 2]

        self.assertEqual(len(self.rotated_array), len(expected_indices))

        for i, value in enumerate(expected_indices):
            expected_idx = expected_indices[i]
            target = i + 1
            result = find_the_target_in_a_rotated_sorted_array(self.rotated_array, target)

            print(f"value({target}) -> idx({result}) -> expectedIdx({expected_idx})")

            self.assertEqual(expected_idx, result)


if __name__ == '__main__':
    unittest.main()
