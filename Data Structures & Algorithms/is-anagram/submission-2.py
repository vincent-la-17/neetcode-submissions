class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (set(s) != set(t)):
            return False
        uniques = set(s)
        for a in uniques:
            if s.count(a) != t.count(a):
                return False
        return True

        