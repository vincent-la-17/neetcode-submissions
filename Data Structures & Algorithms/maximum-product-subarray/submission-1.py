class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1,1
        for num in nums:
            tempHigh = currMax * num
            tempLow = currMin * num
            #num could be negative
            currMax = max(tempHigh, tempLow, num)
            currMin = min(tempHigh, tempLow, num)
            res = max(res, currMax, currMin)
        return res