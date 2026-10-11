class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ledict = {}
        res = []
        for s in strs:
            sig = [0] * 26
            for i in s:
                sig[ord(i) - ord('a')] +=1
            key = tuple(sig)
            if key in ledict:
                ledict[key].append(s)
            else:
                ledict[key] = [s]
        for key in ledict:
            res.append(ledict[key])
        return res
        