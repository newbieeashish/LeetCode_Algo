'''
Implement function ToLowerCase() that has a string parameter str, and 
returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
'''
def toLowerCase(s):
    new_str = ''
    for char in s:
        if 64 < ord(char)<91:
            new_str += chr(ord(char)+32)
        
        else:
            new_str+=char
    return new_str

print(toLowerCase('hEre'))