"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array."""

from xmlrpc.client import MININT


def max_subarr(arr):
    suma=maxim=MININT
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            suma=sum(arr[i:j+1])
            if suma>maxim:
                maxim=suma
    return maxim

arr=[1,2,3,-10,9,-11,8,]

print(max_subarr(arr))
