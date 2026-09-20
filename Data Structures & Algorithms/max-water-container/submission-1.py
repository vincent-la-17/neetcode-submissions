class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0 
        left = 0
        right = len(heights)-1
        width = right-left
        while left < right:
            #min because if you take the larger of the two the water will spill
            currWater = width * min(heights[left], heights[right])
            if heights[left] <= heights[right]:
                left+=1
            else:
                right-=1
            width = right-left
            currMax = max(currMax, currWater)
        return currMax