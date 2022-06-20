#Given a string s, find the length of the longest substring without repeating characters.
def longest_substring(string):
    
    character_set=set()
    left=0
    result=0

    for right in range(len(string)):
        while string[right] in character_set:
            character_set.remove(string[left]) 
            l+=1
        character_set.add(string[right]) 
        result=max(result, right-left+1)
    return result

"""string="abcdefabcabbcdefghijklmn"
print(longest_substring(string))"""
