from typing import List

input_nums = [-5, -2, 3, 4, 6]
target = 7


def pair_sum_sorted(nums: List[int], target_sum: int) -> List[int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target_sum:
            return [left, right]
        elif sum < target_sum:
            left += 1
        elif sum > target_sum:
            right -= 1

    return []


result = pair_sum_sorted(input_nums, target)

print(result)
