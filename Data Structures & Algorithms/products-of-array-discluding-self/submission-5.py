class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        for j in range(len(nums)):
            result[j] *= prefix
            prefix *= nums[j]
         
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
             result[j] *= postfix
             postfix *= nums[j]
           
        return result