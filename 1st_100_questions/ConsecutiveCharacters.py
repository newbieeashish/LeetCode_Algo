'''
Given a string s, the power of the string is the maximum length of a 
non-empty substring that contains only one unique character.
Return the power of the string.
Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1
'''

def ConsecutiveCharacter(s):
    N = len(s)
    if N < 2:
        return N # if len == 0 or 1 then just return that value

    power = 1 # minimum power is 1
    i = 0
    while i < N - power: # stop before len - power
        j = 1
        while i + j < N and s[i + j] == s[i]:
            j += 1 # increase second pointer while symbol the same
        power = max(power, j)
        i += j # move first pointer to position where second pointer stopped
    return power
        

print(ConsecutiveCharacter('"leetcode"'))
        

