from typing import List

input_nums = [-5, -2, 3, 4, 6]
expected_output = [3, 4]

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


def pair_sum_sorted_naive(nums: List[int], target_sum: int) -> List[int]:
    left = 0

    while left < len(nums) - 2:

        right = left + 1

        while right < len(nums) - 1:
            sum = nums[left] + nums[right]

            if sum == target_sum:
                return [left, right]

            right += 1

        left += 1

    return []


result1 = pair_sum_sorted(input_nums, target)

print(f"Input: {input_nums}")
print(f"Expected output: {expected_output}")

print("Solution #1 output")
print(result1)

result2 = pair_sum_sorted_naive(input_nums, target)

print("Solution #2 output")
print(result2)
