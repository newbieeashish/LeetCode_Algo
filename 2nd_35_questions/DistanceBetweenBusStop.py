'''
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the 
distance between all pairs of neighboring stops where distance[i] is the
distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.

Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.
'''

def DistanceBetweenBusStop(distance, start, destination):
    S = min(start, destination)
    D = max(start, destination)
    return min(sum(distance[S:D]), sum(distance) - sum(distance[S:D]))

print(DistanceBetweenBusStop([1,2,3,4],0,3))


