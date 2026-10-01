class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # If nums[left] < nums[mid], the left half is sorted.
            elif nums[left] <= nums[mid]:

                # If the target is greater than nums[mid], it must be
                # in the right half. If the target is less than nums[left],
                # it cannot be in the sorted left half, so search right.
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1

                # Otherwise, the target lies within the sorted left half.
                else:
                    right = mid - 1

            else:
                # Otherwise, the right half must be sorted.
                # If the target is less than nums[mid], it must be
                # in the left half. If the target is greater than nums[right],
                # it cannot be in the sorted right half, so search left.
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1

                # Otherwise, the target lies within the sorted right half.
                else:
                    left = mid + 1

        return -1