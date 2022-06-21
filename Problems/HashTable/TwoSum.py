"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def two_sum(arr, target):

    complement_dict=dict()

    for i in range(len(arr)):
        complement=target-arr[i]
        if arr[i] in complement_dict:
            return complement_dict[arr[i]],i
        else:
            complement_dict[complement]=i
            print(complement_dict)
            
   """
arr=[2,7,11,15]
target=17 

print(two_sum(arr, target))
   """
