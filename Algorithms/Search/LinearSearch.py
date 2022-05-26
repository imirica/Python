# If x is present then return its location
# else return -1
 
 
def search(arr, x):
 
    for i in range(len(arr)):
        if (arr[i] == x):
            return i
    return -1
 
 
"""EXAMPLE

arr = [2, 3, 4, 10, 40]
x = 40
 
result = search(arr, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
"""
