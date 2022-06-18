#Given a string s, find the length of the longest substring without repeating characters.
def longest_substring(string):
    
    character_set=set()
    l=0
    result=0

    for r in range(len(string)):
        while string[r] in character_set:
            character_set.remove(string[l]) 
            l+=1
        character_set.add(string[r]) 
        result=max(result, r-l+1)
    return result

"""string="abcdefabcabbcdefghijklmn"
print(longest_substring(string))"""
