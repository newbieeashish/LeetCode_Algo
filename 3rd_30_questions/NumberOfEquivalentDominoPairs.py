'''
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to 
dominoes[j] = [c, d] if and only if either (a==c and b==d), or
(a==d and b==c) - that is, one domino can be rotated to be equal 
to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < 
dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
'''

def numEquivalentDomino(dominoes):
    cntlist = [0] * 100
    res = 0
    for d1, d2 in dominoes:
        ds = d1 * 10 + d2 if d1 > d2 else d2 * 10 + d1 # Compute hash keys
        tmp = cntlist[ds] # Slight speed improvement
        res += tmp # This way is faster than computing nC2
        cntlist[ds] = tmp + 1
    return res

print(numEquivalentDomino([[1,2],[2,1],[3,4],[5,6]]))