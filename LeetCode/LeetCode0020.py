# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is a valid paranthesis.

def is_valid_parentheses(s):
    stack = []  # Stack to store opening parentheses

    # Define the mapping of opening and closing parentheses
    parentheses_map = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    # Iterate through each character in the string
    for char in s:
        if char in parentheses_map:
            # If the character is an opening parentheses, push it to the stack
            stack.append(char)
        else:
            # If the character is a closing parentheses:
            if not stack or parentheses_map[stack.pop()] != char:
                # If the stack is empty or the popped opening parentheses does not match the current closing parentheses,
                # the string is not valid
                return False

    # If the stack is empty at the end, all parentheses have been properly closed
    return len(stack) == 0
