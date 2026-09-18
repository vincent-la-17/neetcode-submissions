# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def nodeDepth(root):
            nonlocal max_diameter

            if root is None:
                return 0

            left = nodeDepth(root.left)
            right = nodeDepth(root.right)

            # Diameter passing through this node
            max_diameter = max(max_diameter, left + right)

            # Return height of this node
            return 1 + max(left, right)
      
        nodeDepth(root)
        return max_diameter
