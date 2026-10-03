# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        #if both values are smaller than current node; have to move to left subtree
        if (max(p.val, q.val) < root.val):
             return self.lowestCommonAncestor(root.left, p, q)
        #elif both values are bigger than current node; have to move to right subtree
        elif min(p.val, q.val) > root.val:
             return self.lowestCommonAncestor(root.right, p, q)
        #otherwise the current node is the split point
        else:
            return root