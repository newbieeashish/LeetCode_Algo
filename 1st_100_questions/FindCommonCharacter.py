'''
Given an array A of strings made only from lowercase letters, return a 
list of all characters that show up in all strings within the list 
(including duplicates).  For example, if a character occurs 3 times in
 all strings but not 4 times, you need to include that character three 
times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
'''

from collections import Counter
def FindCommonCharacter(A):
    frist = A[0]
    mycount = dict(Counter(frist))
    ouput = []
    for k, v in mycount.items():
        occ =1
        for x in range(1,len(A)):
            if k in A[x]:
                occ +=1
                b = dict(Counter(A[x]))
                count = min(v,b[k])
                v = count
            else:
                break
        if occ == len(A):
            for y in range(0,count):
                ouput.append(k)
    return ouput


print(FindCommonCharacter(["bella","label","roller"]))
