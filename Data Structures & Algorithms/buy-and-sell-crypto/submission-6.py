class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        curr_max = 0
      
        while right < len(prices):
           
            if  prices[left] < prices[right]:
               curr_max = max(prices[right]-prices[left], curr_max)
               
            else:
                left = right
            right+=1
        return curr_max