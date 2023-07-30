"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity."""

def find_insert_position(arr, start, end, target):
    # Calculate the mid index of the current range
    mid = (start + end) // 2

    # Base case: If the start index exceeds the end index, it means the target is not found.
    if start > end:
        # In this case, return the start index, which represents the position where the target should be inserted.
        return start

    # If the middle element matches the target, return its index.
    elif arr[mid] == target:
        return mid

    # If the middle element is greater than the target, search in the left half of the array.
    elif arr[mid] > target:
        return find_insert_position(arr, start, mid - 1, target)

    # If the middle element is smaller than the target, search in the right half of the array.
    else:
        return find_insert_position(arr, mid + 1, end, target)
