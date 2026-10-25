# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #base case
        if root == None:
            return
        
        #invert
        left = root.right
        right = root.left

        #assign
        root.left = left
        root.right = right

        #go down
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
