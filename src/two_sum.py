"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    storage = {}
    for i in range(len(nums)):
        if target - nums[i] in storage:
            return [i, storage[target - nums[i]]]
        storage[nums[i]] = i


nums = [3, 2, 4]
target = 6

res = twoSum(nums, target)
print(res)