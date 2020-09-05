'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the 
array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
def ContainsDuplicate(nums):
    freq = {}
    flag = 1
    for num in nums:
        freq[num] = freq.get(num,0)+1
    
    for k,v in freq.items():
        
        if v >1:
            
            flag = 1
            return True
        else:
            flag = 0
    if flag == 0:
        return False
       
print(ContainsDuplicate([1,2,3,4]))

