import unittest
from typing import List
from unittest import TestCase


def next_largets_number_to_the_right(nums: List[int]) -> List[int]:
    result = [0] * len(nums)

    stack = []
    for i, value in reversed(list(enumerate(nums))):

        while stack and stack[-1] <= value:
            stack.pop()

        result[i] = stack[-1] if len(stack) > 0 else -1

        print("stack:", stack, "<-", value)
        print("input:", nums)
        print("result:", result)
        print()

        stack.append(value)

    return result


class Test(TestCase):
    def test_next_largets_number_to_the_right(self):
        nums = [1, 1, 2, 3, 2, 3, 2, 4]
        expected_result = [2, 2, 3, 4, 3, 4, 4, -1]
        result = next_largets_number_to_the_right(nums)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
