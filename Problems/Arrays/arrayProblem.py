"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
Example:
    Given nums = [12, 23, 33, 124], target = 136,
    Because nums[0] + nums[3] = 12 + 124 = 136,
    return (0, 3)
"""


def two_sum(arr, target):
    dic = {}
    for i, num in enumerate(arr):
        if num in dic:
            return dic[num], i
        else:
            dic[target - num] = i
    return None
