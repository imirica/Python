"""
Given a sorted array of integers arr and an integer target, find the index of the first and the last position of target in arr.
If target can't be found return [-1,-1]
"""

def first_last(arr,target):
    if target>arr[len(arr)-1]:
        return [-1,-1]
    target_values=0
    for i in range(len(arr)):
        if arr[i]==target:
            last=i
            target_values+=1
    return[last-target_values+1, last]


"""
def first_last(arr, target):
    for i in range(len(arr)-1):

        if arr[i]==target:
            start=i
            while i+1<len(arr) and arr[i+1]==target:
                i+=1
            return [start,i]
    return [-1,-1]

"""
