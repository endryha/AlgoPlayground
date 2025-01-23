import unittest
from unittest import TestCase


def count_anagrams(text: str, substr: str) -> int:
    text_len, substr_len = len(text), len(substr)

    if substr_len > text_len:
        return 0

    expected_vector = [0] * 26
    window_vector = [0] * 26

    for c in substr:
        idx = ord(c) - ord('a')
        expected_vector[idx] += 1

    count, left, right = 0, 0, 0
    ignored_chars = 0
    while right < text_len:
        if text[right] == ' ':
            right += 1
            ignored_chars += 1
            continue

        if text[left] == ' ':
            left += 1
            ignored_chars -= 1
            continue

        window_vector[ord(text[right]) - ord('a')] += 1

        if right - left + 1 - ignored_chars == substr_len:
            if expected_vector == window_vector:
                count += 1

            window_vector[ord(text[left]) - ord('a')] -= 1
            left += 1

        right += 1

    return count


class TestAnagrams(TestCase):
    def test_count_anagrams(self):
        self.assertEqual(count_anagrams(text="abccbabacdbbac", substr="abc"), 4)

    def test_count_anagrams_with_whitespaces(self):
        self.assertEqual(count_anagrams(text="abc cba bac  dbb a  c", substr="abc"), 4)


if __name__ == '__main__':
    unittest.main()
