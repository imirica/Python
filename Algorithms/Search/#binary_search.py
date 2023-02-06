#binary_search

import math

def binary_search(arr, start, end, target):

    mid = math.floor((start+end)/2)

    if start>end: return False
    elif arr[mid] == target: return f'the target has been found to position {mid}.'
    elif arr[mid] > target : return binary_search (arr, start, mid-1, target)
    else : return binary_search (arr, mid+1, end, target)


arr = [1,2,3,44,55,66,77,88,99]
start = 0
end = len(arr)
target =  88

print (binary_search(arr, start, end, target))