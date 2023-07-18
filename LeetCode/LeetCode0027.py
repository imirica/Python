#Remove Element

def remove_element(arr, target):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == target:
            arr.pop(i)
            n -= 1
        else:
            i += 1
    return arr
