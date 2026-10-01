# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(root, maxVal):
            #reach the end of branch
            if not root:
                return 0
            #count if good node
            res = 1 if root.val >= maxVal else 0
            #in the new subtree, maxVal is either the ancestor's max value or the current max value
            maxVal = max(root.val, maxVal)
            #recur for left, right trees
            res+=dfs(root.left, maxVal)
            res+=dfs(root.right, maxVal)
            return res

        return dfs(root, root.val)