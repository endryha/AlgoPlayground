import unittest
from unittest import TestCase


def longest_substring_with_unique_chars(text: str) -> str:
    left = right = 0
    max_left = max_right = 0

    frequencies = [0] * 26

    while right < len(text):
        right_idx = ord(text[right]) - ord('a')

        if frequencies[right_idx] > 0:
            left_idx = ord(text[left]) - ord('a')
            frequencies[left_idx] -= 1
            left += 1
        else:
            frequencies[right_idx] += 1
            max_len = max_right - max_left + 1
            current_len = right - left + 1
            if max_len < current_len:
                max_left, max_right = left, right

            right += 1

    return text[max_left:max_right + 1]


def longest_substring_with_unique_chars_optimized(text: str) -> str:
    left = right = 0
    max_left = max_right = 0

    prev_indexes = {}

    while right < len(text):
        c = text[right]
        if c in prev_indexes and prev_indexes[c] >= left:
            left = prev_indexes[c] + 1
        else:
            if max_right - max_left <= right - left:
                max_left, max_right = left, right
        prev_indexes[c] = right
        right += 1

    return text[max_left:max_right + 1]


class Test(TestCase):
    def test_longest_substring_with_unique_chars(self):
        line = "abcbadaaaxyabaaqwer"
        output = longest_substring_with_unique_chars(line)
        print(f"{output} (length: {len(output)})")
        self.assertEqual(5, len(output))

    def test_longest_substring_with_unique_chars_optimized(self):
        line = "abcbadaaaxyabaaqwerh"
        output = longest_substring_with_unique_chars_optimized(line)
        print(f"{output} (length: {len(output)})")
        self.assertEqual(6, len(output))

if __name__ == '__main__':
    unittest.main()