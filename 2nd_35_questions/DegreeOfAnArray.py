'''
Given a non-empty array of non-negative integers nums, the degree of this array is 
defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of 
nums, that has the same degree as nums.
Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
'''
def DegreeOfAnArray(nums):
    dic = {}
    for i, num in enumerate(nums):
        if num not in dic:
            dic[num] = [i]

        else:
            dic[num].append(i)
    
    MAX = 0
    output = []
    for key, value in dic.items():
        if len(value)>MAX:
            MAX = len(value)
            output = [key]
        elif MAX ==1:
            output.append(key)
    MIN = float('inf')
    for num in output:
        MIN = min((dic[num])[-1] - (dic[num])[0] +1, MIN)
    return MIN

print(DegreeOfAnArray([1,2,2,3,1,4,2]))