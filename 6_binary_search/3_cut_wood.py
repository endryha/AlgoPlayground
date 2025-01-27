from typing import List


def cutting_wood(heights: List[int], min_cut_length: int) -> int:
    left, right = 0, max(heights)

    while left < right:
        mid = (left + right) // 2 + 1
        wood_cut_count = count_wood_cut(heights, mid)
        if min_cut_length >= wood_cut_count:
            right = mid
        else:
            left = mid + 1

    return right


def count_wood_cut(heights: List[int], cut_height: int) -> int:
    wood_collected = 0

    for height in heights:
        if height > cut_height:
            wood_collected += height - cut_height

    return wood_collected


heights = [2, 6, 3, 8]
min_cut_length = 7

result = cutting_wood(heights, min_cut_length)
