class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxl = 0
        seen = set()
        res = ""

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                maxl = max(maxl, right - left + 1)
                right += 1
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
   
        return maxl