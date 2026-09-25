class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            totalTime = 0
            mid = (left + right) // 2
            for pile in piles:
                totalTime += math.ceil(pile/mid)
            if totalTime <= h:
                res = mid
                right = mid -1
            else:
                left = mid + 1
        return res
