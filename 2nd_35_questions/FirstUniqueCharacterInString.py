'''
Given a string, find the first non-repeating character in it and return its index. 
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

'''
def FirstUniqueCharacter(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char,0)+1
    
    for key, value in freq.items():
        if value == 1:
            return s.index(key)
            break
    else:
        return -1

    

print(FirstUniqueCharacter("loveleetcode"))