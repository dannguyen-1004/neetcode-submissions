# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.heightAndIsBalance(root)[1]
    
    def heightAndIsBalance(self, root):

        #no child
        if (root.left is None) and (root.right is None):
            return (0, True)

        #left child
        if root.left and (root.right is None):
            d = self.heightAndIsBalance(root.left)
            return (d[0] + 1, d[1] and (d[0] +1 <= 1))

        #right child
        if root.right and (root.left is None):
            d = self.heightAndIsBalance(root.right)
            return (d[0] + 1, d[1] and (d[0] +1 <= 1))

        #both child
        if root.left and root.right:
            dLeft = self.heightAndIsBalance(root.left)
            dRight = self.heightAndIsBalance(root.right)

            return (1 + max(dLeft[0], dRight[0]), dLeft[1] and dRight[1] and abs(dLeft[0] - dRight[0]) <= 1)
    
