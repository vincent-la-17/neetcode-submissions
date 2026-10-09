class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # If nums is empty, return an empty list
        if not nums:
            return []

        res = []       # Stores all possible subsets
        subset = []    # Stores the current subset being built

        def dfs(i):
            # Base case: all elements have been considered
            if i >= len(nums):
                # Add a copy of the current subset to the results
                res.append(subset.copy())
                return

            # Choice 1: Include nums[i] in the current subset
            subset.append(nums[i])
            dfs(i + 1)  # Move to the next element

            # Backtrack: Remove nums[i] to undo the previous choice
            subset.pop()

            # Choice 2: Exclude nums[i] from the current subset
            dfs(i + 1)  # Move to the next element without nums[i]

        # Start DFS at index 0
        dfs(0)

        # Return all possible subsets
        return res