'''
Given a string S and a character C, return an array of integers representing 
the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
'''
def shortestDistance(S,C):
    index_list = []
    for i in range(len(S)):
        if S[i] == C:
            index_list.append(i)
    
    output = []
    for j in range(len(S)):
        output.append(min(abs(j-x) for x in index_list))
    
    return output

print(shortestDistance("loveleetcode",'e'))