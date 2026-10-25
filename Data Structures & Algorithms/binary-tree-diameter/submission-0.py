# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diaAndHeight(root)[0]
    
    def diaAndHeight(self, root):
        #base case:
        if root.left is None and root.right is None:
            return (0, 0)
        
        if root.left and root.right is None:
            d = self.diaAndHeight(root.left)
            return (max(d[0], d[1] + 1), d[1] + 1)

        if root.right and root.left is None:
            d = self.diaAndHeight(root.right)
            return (max(d[0], d[1] + 1), d[1] + 1)

        if root.right and root.left:
            dRight = self.diaAndHeight(root.right)
            dLeft = self.diaAndHeight(root.left)
            return (max(dRight[0], dLeft[0], dRight[1] + dLeft[1] + 2
), 1 + max(dRight[1], dLeft[1]) )

