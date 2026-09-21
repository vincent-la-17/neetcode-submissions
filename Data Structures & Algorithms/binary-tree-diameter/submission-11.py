# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
         # DFS returns the height of the subtree rooted at root
        def dfs(root):
            nonlocal max_diameter
            if root is None:
                return 0

            
            left = dfs(root.left)
            right = dfs(root.right)
            # The diameter passing through this node is:
            # height of left subtree + height of right subtree
            max_diameter = max(max_diameter, left+right)
            # Return the height of the current subtree
            # +1 accounts for the current node
            return 1+max(left, right)
        dfs(root)
        return max_diameter