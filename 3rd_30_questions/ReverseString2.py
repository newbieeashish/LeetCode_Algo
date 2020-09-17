'''
Given a string and an integer k, you need to reverse the first 
k characters for every 2k characters counting from the start 
of the string. If there are less than k characters left, 
reverse all of them. If there are less than 2k but greater 
than or equal to k characters, then reverse the first k characters 
left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
'''

def ReverseString(s,k):
    output=""
    i=0
    while i<len(s):
        bg=s[i:i+k]
        output=output+bg[::-1]+s[i+k:i+2*k]
        i+=2*k
    return output

print(ReverseString('abcdefg',2))