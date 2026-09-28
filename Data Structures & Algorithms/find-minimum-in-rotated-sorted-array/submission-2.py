class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Start with the entire array as the search range
        left = 0
        right = len(nums) - 1

        # Keep track of the minimum value found
        res = nums[0]

        # Continue until left and right point to the same element
        while left < right:

            # Find the middle index
            mid = (left + right) // 2

            # If the middle value is less than the rightmost value,
            # the minimum must be at mid or somewhere to its left.
            if nums[mid] < nums[right]:
                right = mid

            # Otherwise, the minimum must be somewhere to the right of mid.
            else:
                left = mid + 1

        # When left == right, we've found the index of the minimum
        return nums[left]