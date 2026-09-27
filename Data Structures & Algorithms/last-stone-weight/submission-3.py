class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-a for a in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, -(stone1-stone2))
        if len(stones) == 0:
            return 0
        return -stones[0]
