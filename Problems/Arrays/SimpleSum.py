#Display the sum of all the elements of a given array

def arraySum(arr):
    arrsum=0
    for i in range(len(arr)):
        arrsum+=arr[i]
    return arrsum
print(arraySum([1,2,3,4,5]))
