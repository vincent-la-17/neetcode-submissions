class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        left = 0
        right = 1
        curr_max = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                curr_max = max(curr_max, prices[right] - prices[left])
            else:
                #move this because the new best buying price is wherever right is
                left = right
            right +=1
        return curr_max
