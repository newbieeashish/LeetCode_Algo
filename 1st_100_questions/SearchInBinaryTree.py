'''Given the root node of a binary search tree (BST) and a value. You need 
to find the node in the BST that the node's value equals the given value. 
Return the subtree rooted with that node. If such node doesn't exist, you 
should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no 
node with value 5, we should return NULL.'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def searchBST(root, val):
        curr = root

        while curr is not None:
            if  curr.val ==val:
                return curr
            elif curr.val >val:
                curr = curr.left
            else:
                curr = curr.right
            
        return None
