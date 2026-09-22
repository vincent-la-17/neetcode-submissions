class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        total = 0 
        currDigit = 0
        while total not in seen:
            seen.add(n)
            total = 0
            while (n>0):
                currDigit = n%10
                total += currDigit ** 2
                n = n//10
            if total == 1:
                return True
            n = total
        return False