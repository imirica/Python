"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits."""

def plus_one(digits):
    # Start from the last digit (least significant digit)
    index = len(digits) - 1
    carry = 1  # Initialize carry to 1 since we want to add one

    while index >= 0 and carry > 0:
        # Add the carry to the current digit
        digits[index] += carry

        # Calculate the new carry and update the current digit
        carry = digits[index] // 10
        digits[index] %= 10

        # Move to the previous digit (if not already at the first digit)
        index -= 1

    # If there is still a carry left after the loop, it means the most significant digit needs to be extended
    if carry > 0:
        digits.insert(0, carry)

    return digits

arr = [9, 9, 9, 9]
print(plus_one(arr))


"""naive approach

def plus_one(arr):
    joined_string = ''.join(str(num) for num in arr)
    integer = int(joined_string) + 1
    result = []
    for character in str(integer):
        result.append(character)
    return result

"""
