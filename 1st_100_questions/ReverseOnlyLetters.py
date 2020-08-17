'''
Given a string S, return the "reversed" string where all characters that 
are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
'''
def getReverse(S):
    for c in (z for z in reversed(S) if z.isalpha()):
        yield c
            
def reverseOnlyLetters( S):
    gr = getReverse(S)
    return "".join(next(gr) if c.isalpha() else c for c in S)

print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))