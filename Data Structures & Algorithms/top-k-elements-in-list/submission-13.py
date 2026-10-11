class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        for j in nums:
            tracker[j] = tracker.get(j,0) + 1
        res = sorted(tracker, key = tracker.get, reverse = True)
        print(res)
        return res[:k]