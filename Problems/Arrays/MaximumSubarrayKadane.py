"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

def max_subarr(arr):

    suma=0
    maxim=arr[0]
    index=0
    for i in range(len(arr)):
        suma+=arr[i]

        if(maxim<suma):
            maxim=suma
            st=index
            en=i
        if(suma<0):
            suma = 0
            index=i+1

    return maxim, st, en
