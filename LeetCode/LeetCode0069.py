#use binary search to find the 'mid' that multiplied with itself == x

def square_root(x):
    if x == 0:
        return 0

    left, right = 1, x
    while left <= right:
        mid = (right + left) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1

    return right
