"""Given an integer x, return true if x is a palindrome, and false otherwise."""

def palindrom(number):
    return True if str(number) == str(number)[::-1] else False
