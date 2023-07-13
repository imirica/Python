"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""


def two_sum(arr, target):

    dict = {}

    for i in range(len(arr)):
        if target - arr[i] in dict:
            return f"the elements that adds up to the target have been found at positions : '{i}' and '{dict[target - arr[i]]}'"
        dict[arr[i]] = i
    return "404"
