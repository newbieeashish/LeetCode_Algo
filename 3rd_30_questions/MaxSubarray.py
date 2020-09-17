'''
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and 
return its sum.

Follow up: If you have figured out the O(n) solution, try coding 
another solution using the divide and conquer approach, which is 
more subtle.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647

'''

def MaxSubarray(nums):
    sub_sum = 0                     # keep track of the sum of the sub array at each step
        
    max_sum_seen = nums[0]          # keep track of the biggest sum so far
        
    for num in nums:                # for each number in the array
            
        sub_sum += num              # add the number to the current sub_sum
            
        if sub_sum > max_sum_seen: 
                
            max_sum_seen = sub_sum  # reset the max sum if the sub sum is greater
            
        if sub_sum < 0:             # if the sub sum dips into the negatives
                
            sub_sum = 0             # start a new sub array
        
    return max_sum_seen

print(MaxSubarray([-2147483647]))