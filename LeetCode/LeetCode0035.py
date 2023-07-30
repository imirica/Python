"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity."""

def binary_search(arr, start, end, target):

    mid = (start + end) // 2

    if start > end : return start
    elif arr[mid] == target: return mid
    elif arr[mid] > target: return binary_search(arr, start, mid - 1, target)
    else: return binary_search(arr, mid + 1, end, target)
