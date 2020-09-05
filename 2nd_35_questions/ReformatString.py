'''
Given alphanumeric string s. (Alphanumeric string is a string consisting of 
lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by 
another letter and no digit is followed by another digit. That is, no two adjacent 
characters have the same type.

Return the reformatted string or return an empty string if it is impossible to 
reformat the string.

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". 
"a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
Example 4:

Input: s = "covid2019"
Output: "c2o0v1i9d"
Example 5:

Input: s = "ab123"
Output: "1a2b3"
'''
def ReformatString(s):
    a_group, b_group = [], []
    for char in s:
        if 96 < ord(char) < 123: # same as if 'a' <= char <= 'z'
            a_group.append(char)
        else:
            b_group.append(char)

    if len(a_group) < len(b_group): # if the second group length is higher we swap
        a_group, b_group = b_group, a_group

    if len(a_group) - len(b_group) > 1: # if the length difference is more than one, not possible, return ''
        return ''

    reformatted = ''
    for index in range(len(a_group) + len(b_group)):
        if not index & 1:
            reformatted += a_group[index >> 1]
        else:
            reformatted += b_group[index >> 1]

    return reformatted

print(ReformatString('ab123'))