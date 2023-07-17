#Write a function to find the longest common prefix string amongst an array of strings.

import math

def lgp(arr):

    #sort the array
    arr.sort()

    # Take the first and the last element of the sorted array
    first_element = arr[0]
    last_element = arr[-1]

    # Initialize the longest common prefix as an empty string
    longest_common_prefix = ""

    # Iterate over the characters of the first and last elements
    for i in range(min(len(first_element), len(last_element))):
        # If the characters at the same index are equal, append it to the prefix
        if first_element[i] == last_element[i]:
            longest_common_prefix += first_element[i]
        else:
            # If characters are not equal, break the loop
            break

    # Return the longest common prefix
    return longest_common_prefix
