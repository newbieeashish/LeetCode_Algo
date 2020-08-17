'''
Given an integer n, return any array containing n unique integers such that 
they add up to 0.

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
'''

def NuniqueIntegers(n):
    if n % 2 != 0:
        res = [i for i in range(-(n-1)//2, (n-1)//2 + 1, 1)]
    else:
        res = [i for i in range(-n//2, n//2 + 1, 1)]
        res.remove(0)
    return res

print(NuniqueIntegers(5))