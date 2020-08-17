'''
Given an integer array sorted in non-decreasing order, there is exactly one 
integer in the array that occurs more than 25% of the time.

Return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
'''

def ElementAppearance(arr):
    top = .25*len(arr)
    num_count = {}
    for num in arr:
         num_count[num] = num_count.get(num,0)+1
    for k,v in num_count.items():
        if v>top:
            return k    
    

print(ElementAppearance([1,2,2,6,6,6,6,7,10]))