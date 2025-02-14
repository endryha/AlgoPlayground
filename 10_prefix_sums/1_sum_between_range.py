import unittest
from typing import List
from unittest import TestCase


class SumBetweenRange:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

        print("input:", nums, "prefix sum:", self.prefix_sum)

    def sum_range(self, i: int, j: int) -> int:
        if i == 0:
            return self.prefix_sum[j]
        else:
            return self.prefix_sum[j] - self.prefix_sum[i - 1]


class Test(TestCase):
    def test_sum_range_1(self):
        values = [3, -7, 6, 0, -2, 5]

        sum_between_range = SumBetweenRange(values)

        for i in range(len(values)):
            for j in range(len(values)):
                if i <= j:
                    expected = self._sum_range_naive(values, i, j)
                    actual = sum_between_range.sum_range(i, j)

                    print(f"Sum for range {i}..{j} -> expected={expected}, actual={actual}")

                    self.assertEqual(expected, actual)

    def _sum_range_naive(self, nums: List[int], i: int, j: int) -> int:
        result = 0
        for k in range(i, j + 1):
            result += nums[k]
        return result


if __name__ == "__main__":
    unittest.main()
