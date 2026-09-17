class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
    
        for a in strs:
            signature = [0] * 26
            for s in a:
                signature[ord(s) - ord('a')] += 1
            key = tuple(signature)
            if key not in tracker:
                tracker[key] = [a]
            else:
                tracker[key].append(a)
        return list(tracker.values())
