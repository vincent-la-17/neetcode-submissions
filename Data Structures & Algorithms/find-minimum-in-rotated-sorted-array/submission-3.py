class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        res =  nums[0]
        while left < right:
            mid = (left+right)//2 
            #if the right element is larger than middle, it means that 
            #minimum must be to the left of mid.
            if nums[mid] < nums[right]:
                right = mid
            #if the left index element is larger than mid, the right has the minimum.
            else:
                left = mid +1
        return nums[left]