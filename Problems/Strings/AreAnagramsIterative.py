#Given two strings, s1 and s2, check if they are anagrams
#use dictionaries 

def are_anagrams(s1,s2):
    if len(s1)!=len(s2):
        return False

    dict1={}
    dict2={}

    for ch in s1:
        if ch in dict1:
            dict1[ch]+=1
        else:
            dict1[ch]=1

    for ch in s2:
        if ch in dict2:
            dict2[ch]+=1
        else:
            dict2[ch]=1

    for key in dict1:
        if key not in dict2 or dict1[key]!=dict2[key]:
            return False
    return True
