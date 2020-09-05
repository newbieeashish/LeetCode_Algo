'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing 
moving one unit north, south, east, or west, respectively. You start at the 
origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time 
you are on a location you've previously visited. Return False otherwise.

Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

'''

def PathCrossing(path):
    x, y = 0, 0
    seen = {(x, y)}
    for move in path: 
        if   move == "N": y += 1
        elif move == "S": y -= 1
        elif move == "E": x += 1
        else: x -= 1
        if (x, y) in seen: return True
        seen.add((x, y))
    return False 

print(PathCrossing('NESWW'))