'''
A rectangle is represented as a list [x1, y1, x2, y2], where
 (x1, y1) are the coordinates of its bottom-left corner, and 
 (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is 
positive.  To be clear, two rectangles that only touch at 
the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they 
overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
'''

def RectangleOverlap(rec1, rec2):
# (x1, y1) is bottom left corner of rectangle, and (x2, y2) is upper right corner
# use rec2 as base line of rectangle and compare rec1 with rec2
# judge the cases that two recs not intersect：
# 1.  rec1's x2 <= rec2's x1；means rec1 is on the left side of rec2
# 2. rec1's y2 <= rec2's y1；means rec1 is under rec2
# 3. rec2's x2 <= rec1's x1；means rec1 is on the right side of rec2
# 4. rec2's y2 <= rec1's y1；means rec1 is above rec2
    rec1_x1, rec1_y1, rec1_x2, rec1_y2 = rec1
    rec2_x1, rec2_y1, rec2_x2, rec2_y2 = rec2
    return not (rec1_x1 >= rec2_x2 or rec1_x2 <= rec2_x1 or rec1_y1 >= rec2_y2 or rec1_y2 <= rec2_y1)

print(RectangleOverlap([0,0,2,2],[1,1,3,3]))