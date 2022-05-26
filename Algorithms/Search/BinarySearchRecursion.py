"""recursive binary search"""
import math

def binary_search(arr, start, end, target):
    mid=math.floor((start+end)/2)
    if start>end : return False
    elif arr[mid]==target: return mid
    elif arr[mid]>target:return binary_search(arr,start,mid-1,target)
    else: return binary_search(arr, mid+1, end, target)
