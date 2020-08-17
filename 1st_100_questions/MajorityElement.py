'''
Given an array of size n, find the majority element. The majority element is 
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

def MajorityElement(nums):
    count_element = {}
    threshold = len(nums)/2

    for num in nums:
        count_element[num] = count_element.get(num,0)+1

    for k ,v in count_element.items():
        if v>threshold:
            return k

print(MajorityElement([2,2,1,1,1,2,2]))


