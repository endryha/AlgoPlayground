import unittest
from unittest import TestCase


def longest_uniform_substring_after_replacements(s: str, k: int) -> str:
    freq = {}
    highest_freq = max_len = 0
    left = right = 0
    max_left = max_right = 0

    while right < len(s):
        freq[s[right]] = freq.get(s[right], 0) + 1

        highest_freq = max(highest_freq, freq.get(s[right]))

        num_chars_to_replace = right - left + 1 - highest_freq

        if num_chars_to_replace > k:
            freq[s[left]] = freq[s[left]] - 1
            left += 1

        if max_len < right - left + 1:
            max_len = right - left + 1
            max_left, max_right = left, right

        right += 1

    result = s[max_left:max_right + 1]
    # print(max_len)
    # print(result, "->", len(result))

    return result


class Test(TestCase):
    def test_longest_substring_with_unique_chars1(self):
        line = "aabcdccaaxyztv"
        output = longest_uniform_substring_after_replacements(line, 3)
        print(f"{output} → length={len(output)}")
        self.assertEqual(6, len(output))

    def test_longest_substring_with_unique_chars2(self):
        line = "aabcdccaaxyztvqwertyuiopasdfghjklzxcvbnm"
        output = longest_uniform_substring_after_replacements(line, 3)
        print(f"{output} → length={len(output)}")
        self.assertEqual(6, len(output))

    def test_longest_substring_with_unique_chars3(self):
        line = "aabcdccaaxyztvqwertyuiopasdfghjklzxcvbnmuuuuuuu"
        output = longest_uniform_substring_after_replacements(line, 3)
        print(f"{output} → length={len(output)}")
        self.assertEqual(10, len(output))


if __name__ == '__main__':
    unittest.main()
