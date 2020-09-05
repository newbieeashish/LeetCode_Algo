'''
Given two non-negative integers low and high. Return the count of odd numbers 
between low and high (inclusive).

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
'''

def CountOddNumber(low,high):
    count = 0
    for num in range(low, high+1):
        if num%2 !=0:
            count+=1
    return count

print(CountOddNumber(8,10))


#alternate solution
''' count = 0
if low%2==1 or high%2==1:
            count+=1
        return ((high-low)//2)+count

        '''