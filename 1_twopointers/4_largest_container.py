from typing import List

input_heights = [2, 7, 8, 3, 7, 6]
expected_result = 24


def largest_container(heights: List[int]) -> int:
    left = 0
    right = len(heights) - 1

    max_box_size = 0

    while left < right:
        box_size = min(heights[left], heights[right]) * (right - left)

        if box_size > max_box_size:
            max_box_size = box_size

        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1

    return max_box_size


result = largest_container(input_heights)

print(f"Input {input_heights}, expected: {expected_result}, actual: {result}")
