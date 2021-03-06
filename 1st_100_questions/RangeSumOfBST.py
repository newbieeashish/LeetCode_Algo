'''
Given the root node of a binary search tree, return the sum of values of all 
nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23'''

class Solution:
    def rangeSumBST(self, root, L, R):
	    return self.bst(root, L, R)

    def bst(self, root, l, r):
	    if not root:
		    return 0
	    elif root.val<l:
		#all elements in the left will be smaller
		    return self.bst(root.right, l, r)
	    elif root.val>r:
		#all elements in the right will be greater
		    return self.bst(root.left, l, r)
	    elif root.val>=l and root.val<=r:
		    l_sum = self.bst(root.right, l, r)
		    r_sum = self.bst(root.left, l, r)
		    return root.val + l_sum + r_sum

