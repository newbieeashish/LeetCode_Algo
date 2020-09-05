'''
Given an array A of integers, return true if and only if we can partition the 
array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with 
(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + 
A[A.length - 1])

Example 1:

Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
'''
def ThreeEqualParts(A):
    tot_sum = sum(A)
    if tot_sum % 3 != 0:
        return(False)
    else:
        cum_sum = 0
        target = tot_sum//3
        counter = 0
        for num in A[:-1]:
            cum_sum += num
            if cum_sum == target:
                counter += 1
                cum_sum = 0
                if counter == 2:
                    return(True)
        return(False)

print(ThreeEqualParts([3,3,6,5,-2,2,5,1,-9,4]))
