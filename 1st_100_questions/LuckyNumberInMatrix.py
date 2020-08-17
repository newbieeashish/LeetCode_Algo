'''
Given a m * n matrix of distinct numbers, return all lucky numbers in the 
matrix in any order.

A lucky number is an element of the matrix such that it is the minimum 
element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its 
row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row
and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
'''
def LuckyNumber(matrix):
    luckynumber = []
    for i in range(len(matrix)):
        min_value = min(matrix[i])
        min_index = matrix[i].index(min_value)
        max_value = max(row[min_index] for row in matrix)
        if min_value == max_value:
            luckynumber.append(max_value)
    return luckynumber


print(LuckyNumber([[3,7,8],[9,11,13],[15,16,17]]))