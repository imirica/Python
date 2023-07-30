#Given a string s consisting of words and spaces, return the length of the last word in the string.

def length_of_last_word(s):
    return len(s.split()[-1])
