'''
Given scores of N athletes, find their relative ranks and the 
people with the top three highest scores, who will be awarded 
medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest 
scores, so they got "Gold Medal", "Silver Medal" and 
"Bronze Medal". 
For the left two athletes, you just need to output their relative 
ranks according to their scores.
'''

def RelativeRanks(nums):
    nums_sorted = sorted(nums, reverse=True)

    output = []

    for i in range(len(nums)):
        temp_rank = nums_sorted.index(nums[i]) + 1
        if temp_rank == 1:
            temp_rank = 'Gold Medal'
        elif temp_rank == 2:
            temp_rank = 'Silver Medal'
        elif temp_rank == 3:
            temp_rank = 'Bronze Medal'
        output.append(str(temp_rank))
    return output


print (RelativeRanks([5, 4, 3, 2, 1]))
        