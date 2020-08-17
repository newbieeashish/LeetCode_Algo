'''
Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]'''

def MoveZeroes(nums):


    
    for num in nums:
        if num ==0:
            nums.pop(nums.index(num))
            nums.append(0)



    return nums

print(MoveZeroes([0,1,0,3,12]))