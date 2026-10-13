class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        left = 0
        right = len(heights)-1
        while left < right:
            width = right-left
            currVol = width * min(heights[left], heights[right])
            currMax = max(currVol, currMax)
            if heights[left] <= heights[right]:
                left +=1
            else:
                right -=1
        return currMax