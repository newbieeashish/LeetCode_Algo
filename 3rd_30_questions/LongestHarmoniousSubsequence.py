'''
We define a harmonious array as an array where the difference 
between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest 
harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the 
array by deleting some or no elements without changing the order 
of 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0
'''

def LongestHarmonious(nums):
    nums = sorted(nums)
    n = {}
    for i in nums :
        if i not in  n :
            n[i] = 1
        else:
            n[i] += 1
        #print(n)
    l = list(n.keys())
    m = 0
    for i in range(len(l)-1):
        if l[i+1] -l[i] == 1:
            c = n[l[i]]+n[l[i+1]]
            if c >= m:
                m = c
            
            #print(n[i])
        #print(n.sort())
    return m

print(LongestHarmonious([1,1,1,1]))