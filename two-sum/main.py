from typing import List


class Solution:

    @staticmethod
    def two_sum_by_brute_force(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    @staticmethod
    def two_sum_by_in(nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + i:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

    @staticmethod
    def two_sum_by_map(nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # replace key, value then save to dict
        for i, num in enumerate(nums):
            nums_map[num] = i

        # find by key the result of subtracting the first number from the target
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

    @staticmethod
    def two_sum_by_integrated_for(nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # integrate just one for
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i


if __name__ == '__main__':
    pass
