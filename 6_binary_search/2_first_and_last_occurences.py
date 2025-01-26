import unittest
from typing import List
from unittest import TestCase


def find_first_and_last_occurrences(nums: List[int], target: int) -> List[int]:
    lower_index = find_first_and_last_occurrences_lower(nums, target)

    if lower_index == -1:
        return [-1, -1]


    upper_index = find_first_and_last_occurrences_upper(nums, target)

    return [lower_index, upper_index]


def find_first_and_last_occurrences_lower(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1

    return left if nums[left] == target else -1


def find_first_and_last_occurrences_upper(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[right] == target:
            return right

        mid = (left + right) // 2

        if target >= nums[mid]:
            left = mid
        else:
            right = mid - 1

    return right if nums[right] == target else -1


class Test(TestCase):
    def test_find_first_and_last_occurrences_lower(self):
        nums = [1, 2, 3, 4, 4, 4, 5, 6, 7]
        target = 4
        lower_index = find_first_and_last_occurrences_lower(nums, target)
        print(f"{nums} target: {target} -> lower index: {lower_index}")

        self.assertEqual(3, lower_index)

        target = 0
        lower_index = find_first_and_last_occurrences_lower(nums, target)
        print(f"{nums} target: {target} -> lower index: {lower_index}")

        self.assertEqual(-1, lower_index)

    def test_find_first_and_last_occurrences_upper(self):
        nums = [1, 2, 3, 4, 4, 4, 5, 6, 7]
        target = 4
        lower_index = find_first_and_last_occurrences_upper(nums, target)
        print(f"{nums} target: {target} -> lower index: {lower_index}")

        self.assertEqual(5, lower_index)

        target = 0
        lower_index = find_first_and_last_occurrences_upper(nums, target)
        print(f"{nums} target: {target} -> lower index: {lower_index}")

        self.assertEqual(-1, lower_index)

    def test_find_first_and_last_occurrences(self):
        nums = [1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 6, 7]
        target = 5
        lower_index, upper_index = find_first_and_last_occurrences(nums, target)
        print(f"{nums} ({len(nums)}) target: {target} -> lower index: {lower_index}, upper index: {upper_index}")

        self.assertEqual(6, lower_index)
        self.assertEqual(9, upper_index)

        target = 0
        lower_index, upper_index = find_first_and_last_occurrences(nums, target)
        print(f"{nums} ({len(nums)}) target: {target} -> lower index: {lower_index}, upper index: {upper_index}")

        self.assertEqual(-1, lower_index)
        self.assertEqual(-1, upper_index)


if __name__ == '__main__':
    unittest.main()
