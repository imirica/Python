#merge sorted arrays

def merge_arrays(left, right):

    #left, right index
    li = 0
    ri = 0

    result = []

    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            result.append(left[li])
            li += 1
        else:
            result.append(right[ri])
            ri += 1

    result.extend(right[ri:])
    result.extend(left[li:])

    return result
