'''
Given an array A of integers, for each integer A[i] we may choose any x 
with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and 
the minimum value of B.

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]'''

def SmallestRange(A,K):

    highest_val = max(A)
    lowest_val = min(A)
    diff =  ((highest_val-K)-(lowest_val+K))
    if diff <0:
        diff = 0
    return  diff

print(SmallestRange([1,3,6],3))