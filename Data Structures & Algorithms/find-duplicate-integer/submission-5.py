class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use two pointers to detect a cycle:
        # slow moves one step at a time
        # fast moves two steps at a time
        slow = 0
        fast = 0

        # Move the pointers until they meet inside the cycle
        while slow < len(nums):
            slow = nums[slow]              # Move slow by 1 step
            fast = nums[nums[fast]]        # Move fast by 2 steps

            # If they meet, we have detected a cycle
            if slow == fast:
                break

        # Start a second pointer at the beginning
        # to find the entrance of the cycle.
        slow2 = 0

        while True:
            # Move both pointers one step at a time
            slow = nums[slow]
            slow2 = nums[slow2]

            # Where they meet is the entrance of the cycle,
            # which corresponds to the duplicate number.
            if slow == slow2:
                return slow