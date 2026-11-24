class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while(len(stones) > 1):
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)
            print(stones)
            if s1 == s2:
                continue
            elif s1 > s2:
                new_stone = s1-s2
                heapq.heappush_max(stones, new_stone)
           
        return stones[0] if stones else 0