def merge_sort(array):

    if len(array)<=1:
        return array


    mid = int(len(array)/2)
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left,right)

def merge(left, right):

    result=[]
    left_pointer = right_pointer=0

    while left_pointer<len(left) and right_pointer<len(right):

        if left[left_pointer] < right[right_pointer]:

            result.append(left[left_pointer])
            left_pointer+=1

        else:

            result.append(right[right_pointer])
            right_pointer+=1

        result.extend(left[left_pointer:])
        result.extend(right[right_pointer:])

        return result
