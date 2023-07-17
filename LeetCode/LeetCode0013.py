#Given a roman numeral, convert it to an integer.

def roman_to_numeral(string):

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    previous_value = 0

    # Iterate through the string in reverse order
    for i in range(len(string) - 1, -1, -1):
        current_value = roman_dict[string[i]]

        # If the current value is smaller than the previous value, subtract it
        if current_value < previous_value:
            total -= current_value

        # Otherwise, add it to the total
        else:
            total += current_value

        previous_value = current_value

    return total

#test
print(roman_to_numeral ("MMCCC"))
