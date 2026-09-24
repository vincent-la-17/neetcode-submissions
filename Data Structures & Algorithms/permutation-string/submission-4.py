from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        i = 0
        interval = len(s1)
        uniq = dict(Counter(s1))
        while i < len(s2):
            curr_interval = s2[i:i+interval]
            if dict(Counter(curr_interval)) == uniq:
                return True
            i += 1
        return False