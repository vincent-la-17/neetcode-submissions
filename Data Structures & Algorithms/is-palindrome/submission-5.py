class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = []
        for a in s:
            if a.isalnum():
                chars.append(a)
        cleaned = "".join(chars)    
        print(cleaned)
        left = 0
        right = len(cleaned) - 1
        while (left < right):
        
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True