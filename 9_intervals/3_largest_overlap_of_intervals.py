import unittest
from typing import List
from unittest import TestCase

from interval import create_intervals, draw_intervals, Interval


def largest_overlap_of_intervals(intervals: List[Interval]) -> int:
    if len(intervals) == 0:
        return 0

    points = []
    for interval in intervals:
        points.append((interval.start, 'S'))
        points.append((interval.end, 'E'))
    points = sorted(points, key=lambda x: (x[0], 0 if x[1] == 'E' else 1))

    print(points)

    interval_counter = 0
    max_overlap = 0

    for point, point_type in points:
        if point_type == 'E':
            interval_counter -= 1

        if point_type == 'S':
            interval_counter += 1

        max_overlap = max(max_overlap, interval_counter)

    return max_overlap


class Test(TestCase):
    def test_largest_overlap_of_intervals_empty(self):
        self.assertEqual(0, largest_overlap_of_intervals([]))

    def test_largest_overlap_of_intervals(self):
        intervals = create_intervals([(1, 3), (2, 6), (4, 8), (6, 7), (5, 7)])
        draw_intervals(intervals)
        print()

        result = largest_overlap_of_intervals(intervals)

        self.assertEqual(3, result)


if __name__ == "__main__":
    unittest.main()
