from typing import List

input1 = [-1, 3, 4, 2]
target1 = 3
expected_result1 = [0, 2]


def pair_sum_unsorted(nums: List[int], target_sum: int) -> List[int]:
    cache = {}

    for i in range(len(nums)):
        num = nums[i]
        pair_num = target_sum - num

        if pair_num in cache:
            return [cache[pair_num], i]

        cache[num] = i

    return []


result = pair_sum_unsorted(input1, target1)

print(result)
