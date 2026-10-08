class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Start with the root's value as the largest path sum.
        # This also handles trees where all values are negative.
        largest = root.val

        def dfs(root):
            nonlocal largest

            # An empty subtree contributes nothing to the path.
            if root is None:
                return 0

            # Find the maximum path sum we can get from the left subtree.
            # If it's negative, ignore it by using 0.
            left = max(dfs(root.left), 0)

            # Find the maximum path sum we can get from the right subtree.
            # If it's negative, ignore it by using 0.
            right = max(dfs(root.right), 0)

            # A path passing through the current node can include:
            # left subtree + current node + right subtree.
            largest = max(largest, root.val + left + right)

            # Return the maximum path that can be extended to the parent.
            # We can only continue through one side of the current node.
            return root.val + max(left, right)

        # Recursively visit every node in the tree.
        dfs(root)

        # Return the largest path sum found anywhere in the tree.
        return largest