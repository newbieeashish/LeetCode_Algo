'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a 
tuple of points (i, j, k) such that the distance between i and j equals the 
distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and 
coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''
def NumberOfBoomerangs(points):
    output = 0

    for a,b in points:
        counter = {}
        for x,y in points:
            key = (x-a)**2 + (y-b)**2
            if key in counter:
                output+=2*counter[key]
                counter[key] +=1
            else:
                counter[key] = 1

    return output

print(NumberOfBoomerangs([[0,0],[1,0],[2,0]]))