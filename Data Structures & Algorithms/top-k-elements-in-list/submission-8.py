class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        
    
        for i in nums:
            tracker[i] = tracker.get(i,0) + 1
        result = sorted(tracker, key = tracker.get, reverse = True)
        return result[:k]