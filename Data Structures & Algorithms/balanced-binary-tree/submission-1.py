# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True
        def nodeDepth(root):
            nonlocal balance
            if root is None:
                return 0
            leftH = nodeDepth(root.left)
            rightH = nodeDepth(root.right)
            if abs(leftH - rightH) > 1:
                balance = False
            depth = max(1+leftH, 1+rightH)
            return depth
        nodeDepth(root)
        return balance