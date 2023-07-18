#Remove Duplicates from Sorted Array

def remove_duplicates(arr):
    # i = len(arr) - 1
    # while i > 0:
    #     if arr[i] == arr[i-1]:
    #         arr.pop(i)
    #     i -= 1
    # return arr

    final_arr = []
    for i in range(len(arr)):
        if arr[i] == arr[i-1]:
            continue
        else:
            final_arr.append(arr[i])

    return final_arr
