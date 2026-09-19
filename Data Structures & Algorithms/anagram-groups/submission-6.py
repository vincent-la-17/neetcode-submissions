class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sig = [0] * 26
            for i in s:
                sig[ord(i) - ord('a')] += 1
            key = tuple(sig)
            if key in res.keys():
                res[key].append(s)
            else:
                res[key] = [s]
        return list(res.values())