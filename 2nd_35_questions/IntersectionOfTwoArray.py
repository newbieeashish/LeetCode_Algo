'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
'''

def IntersectionOfTwoArray(nums1, nums2):
    output = []
    for num in nums1:
        if num in nums2:
            nums2.remove(num)
            output.append(num)
    
    return output


print(IntersectionOfTwoArray([4,9,5],[9,4,9,8,4]))