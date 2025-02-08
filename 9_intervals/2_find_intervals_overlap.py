import unittest
from typing import List
from unittest import TestCase

from interval import Interval, draw_intervals, create_intervals


def find_intervals_overlap(intervals1: List[Interval], intervals2: List[Interval]) -> List[Interval]:
    intervals1 = sorted(intervals1, key=lambda interval: interval.start)
    intervals2 = sorted(intervals2, key=lambda interval: interval.start)

    overlaps = []
    i = j = 0

    while i < len(intervals1) and j < len(intervals2):
        if intervals1[i].start <= intervals2[j].start:
            first, second = intervals1[i], intervals2[j]
        else:
            first, second = intervals2[j], intervals1[i]

        if first.end >= second.start:
            overlaps.append(Interval(second.start, min(first.end, second.end)))

        if intervals1[i].end <= intervals2[j].end:
            i += 1
        else:
            j += 1

    return overlaps


class Test(TestCase):

    def test_find_intervals_overlap(self):
        intervals1 = create_intervals([(1, 4), (5, 6), (9, 10)])
        intervals2 = create_intervals([(2, 7), (8, 9)])

        expected_result = create_intervals([(2, 4), (5, 6), (9, 9)])

        print("intervals 1:")
        print(intervals1)
        print("intervals 2:")
        print(intervals2)
        print()
        print("all intervals")
        draw_intervals([*intervals1, *intervals2], start_x_idx=0, end_x_idx=10)

        result = find_intervals_overlap(intervals1, intervals2)
        print()
        print("overlapped intervals:")
        draw_intervals(result, start_x_idx=0, end_x_idx=10)

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
