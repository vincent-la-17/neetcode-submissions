class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        ## add 1 current or default to 1
        for i in nums:
            tracker[i] = tracker.get(i,0) + 1
        reverse = sorted(tracker, key = tracker.get, reverse = True)
        return reverse[:k]