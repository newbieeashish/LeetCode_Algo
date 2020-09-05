'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
'''
def MissingNumber(nums):
    nums.sort()
    for i in range(len(nums)+1):
        if i not in nums:
            return i

print(MissingNumber([0]))


#alternative

'''
def MissingNumber(nums):
    nums_set = set(nums)
    for i in range(len(nums)+1):
        if i not in nums_set:
            return i

print(MissingNumber([0]))
            
