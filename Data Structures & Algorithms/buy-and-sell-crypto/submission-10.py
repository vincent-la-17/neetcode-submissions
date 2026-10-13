class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxCurr = 0
        length = len(prices)
        if length <= 1:
            return 0
        left = 0
        right = 1
        while right < length:
            currProf = prices[right] - prices[left]
            maxCurr = max(currProf, maxCurr)
            if prices[right] < prices[left]:
                left = right
            right +=1
        return maxCurr