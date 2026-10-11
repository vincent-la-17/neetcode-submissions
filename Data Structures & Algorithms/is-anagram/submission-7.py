class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = set(s)
        for i in a:
            if len(a) != len(set(t)):
                return False
            if s.count(i) != t.count(i):
                return False
        return True