class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Negate all stone weights to simulate a max-heap
        stones = [-a for a in stones]

        # Convert the list into a heap
        heapq.heapify(stones)

        # Continue until at most one stone remains
        while len(stones) > 1:

            # Remove the two heaviest stones
            # Negate them to recover their original positive weights
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            # If the weights differ, the lighter stone is destroyed
            # and the heavier stone's remaining weight is their difference
            if stone1 != stone2:

                # Negate the remaining weight before pushing it back
                heapq.heappush(stones, -(stone1 - stone2))

            # If the weights are equal, both stones are destroyed

        # If no stones remain, return 0
        if len(stones) == 0:
            return 0

        # Otherwise, return the last stone's original positive weight
        return -stones[0]