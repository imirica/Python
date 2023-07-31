def add_binary(a, b):
    # Convert binary strings to decimal integers
    int_a = int(a, 2)
    int_b = int(b, 2)

    # Add the decimal integers
    sum_decimal = int_a + int_b

    # Convert the sum back to binary and remove the '0b' prefix
    binary_sum = bin(sum_decimal)[2:]

    return binary_sum

# Example usage:
a = "11"
b = "1"
result = add_binary(a, b)
print(result)  # Output: "100"
