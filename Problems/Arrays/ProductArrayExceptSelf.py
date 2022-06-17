"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


def item_product(arr):
    left=[1]*(len(arr))

    for i in range(len(arr)):

        if i==0:
            continue
        left[i]=left[i-1]*arr[i-1]

    dreapta = [1]*len(arr)

    for j in range(len(arr)-1,-1,-1):

        if j==len(arr)-1:
            continue
        dreapta[j]=dreapta[j+1]*arr[j+1]

    result=[0]*len(arr)
    for i in range(len(arr)):
        result[i]=left[i]*dreapta[i]

    return result

"""
arr=[2,5,3,4]
print(item_product(arr))
"""
