'''
Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.


Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


def SingleNumber(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num,0)+1
    for num, v in count.items():
        if v ==1:
            return num

print(SingleNumber([2,2,1]))


