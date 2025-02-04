import unittest
from typing import List
from unittest import TestCase

from interval import Interval, create_intervals, draw_intervals


def merge_overlapping_intervals(intervals: List[Interval]) -> List[Interval]:
    sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
    result = [sorted_intervals[0]]

    for i in sorted_intervals[1:]:
        merged_interval = result[-1]
        if i.start <= merged_interval.end:
            if i.end > merged_interval.end:
                merged_interval.end = i.end
        else:
            result.append(Interval(i.start, i.end))

    return result


class Test(TestCase):
    def test_merge_overlapping_intervals(self):
        test_intervals = create_intervals([(3, 4), (7, 8), (2, 5), (6, 7), (1, 4)])
        expected_result = create_intervals([(1, 5), (6, 8)])

        draw_intervals(test_intervals)
        print()

        result = merge_overlapping_intervals(test_intervals)

        draw_intervals(result)

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
