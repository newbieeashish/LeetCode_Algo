'''
Given a column title as appear in an Excel sheet, return its corresponding 
column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''

def titleToNumber(s):
    number = 0
    for char in s:
        number = 26*number + ord(char) - ord('A') +1
    return number


print(titleToNumber('ZY'))