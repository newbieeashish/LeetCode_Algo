'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, 
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything
from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified 
to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
'''

def DuplicateZeros(arr):
    idx = 0
    while idx <len(arr):
        if arr[idx] != 0:
            idx+=1
        else:
            arr.insert(idx+1,0)
            idx+=2
            arr.pop()
print(DuplicateZeros([1,0,2,3,0,4,5,0]))
