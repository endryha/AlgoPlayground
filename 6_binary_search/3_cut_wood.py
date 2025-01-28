from typing import List


def cutting_wood(heights: List[int], min_cut_length: int) -> int:
    left, right = 0, max(heights)
    result = -1

    while left <= right:
        height = (left + right) // 2
        wood_cut_count = count_wood_cut(heights, height)

        if wood_cut_count >= min_cut_length:
            result = height
            left = height + 1
        else:
            right = height - 1

    return result


def count_wood_cut(heights: List[int], cut_height: int) -> int:
    wood_collected = 0

    for height in heights:
        if height > cut_height:
            wood_collected += height - cut_height

    return wood_collected


heights = [2, 6, 3, 8]
min_cut_length = 7

result = cutting_wood(heights, min_cut_length)
print(result)