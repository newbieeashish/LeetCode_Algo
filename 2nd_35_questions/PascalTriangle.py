'''
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def PascalTriangle(numRows):
    if numRows ==0:
        return []
    output = [[1],[1,1]]
    if numRows ==1:
        return [output[0]]
    if numRows ==2:
        return output
    
    oldrow = output[-1]  #[1,1]

    for i in range(numRows-2):
        newrow = [1]*(len(oldrow)+1)
        for j in range(1,len(newrow)-1):
            newrow[j] = oldrow[j-1]+oldrow[j]

        output.append(newrow)
        oldrow = newrow
    return output

print(PascalTriangle(5))