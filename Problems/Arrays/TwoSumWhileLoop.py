"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
"""

def two_sum(arr, target):
    pointer_l=0
    pointer_r=len(arr)-1

    while pointer_l<pointer_r:
        sum=arr[pointer_l]+arr[pointer_r]

        if sum==target:
            return pointer_l, pointer_r
        elif sum<target:
            pointer_l+=1
        else:
            pointer_r-=1

    return False

print(two_sum(nums, target))
