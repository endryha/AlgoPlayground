from typing import List

input_nums = [0, -1, 2, -3, 1]
expected_output = [[-3, 1, 2], [-1, 0, 1]]


def pair_sum(nums: List[int], start_idx: int, target: int) -> List[int]:
    left = start_idx
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [nums[left], nums[right]]
    return []


def triplet_sum(nums: List[int]) -> List[List[int]]:
    index = 0

    triplets = []

    while index < len(nums) - 2:
        current_value = nums[index]
        result = pair_sum(nums, index + 1, -current_value)

        if len(result) > 0:
            result.append(nums[index])
            triplets.append(result)

        while nums[index] == current_value:
            index += 1

    return triplets


result = triplet_sum(input_nums)

print(f"Input: {input_nums}")
print(f"Expected output: {expected_output}")

print("Solution output")
print(result)
