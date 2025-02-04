import unittest
from typing import List
from unittest import TestCase

from interval import Interval


def merge_overlapping_intervals(intervals: List[Interval]) -> List[Interval]:
    sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
    print("sorted intervals:")
    print(sorted_intervals)

    result = [sorted_intervals[0]]

    for i in sorted_intervals[1:]:
        merged_interval = result[-1]
        if i.start <= merged_interval.end:
            if i.end > merged_interval.end:
                merged_interval.end = i.end
        else:
            result.append(Interval(i.start, i.end))

    return result


intervals = [Interval(3, 4),
             Interval(7, 8),
             Interval(2, 5),
             Interval(6, 7),
             Interval(1, 4)]


class Test(TestCase):
    def test_merge_overlapping_intervals(self):
        test_intervals = [Interval(3, 4),
                          Interval(7, 8),
                          Interval(2, 5),
                          Interval(6, 7),
                          Interval(1, 4)]

        expected_result = [Interval(1, 5), Interval(6, 8)]

        result = merge_overlapping_intervals(test_intervals)

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
