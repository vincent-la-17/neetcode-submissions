# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True
        def calcDepth(root):
            nonlocal balance
            if (root is None):
                return 0
            leftH = calcDepth(root.left)
            rightH = calcDepth(root.right)
            if abs(leftH - rightH) > 1:
                balance = False
            depth = 1 + max(leftH, rightH)
            return depth
        calcDepth(root)
        return balance