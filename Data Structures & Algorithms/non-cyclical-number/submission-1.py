class Solution:
    def isHappy(self, n: int) -> bool:
        tsum = 0
        currDigit = 0
        seen = set()
        while tsum not in seen:
            seen.add(n)
            tsum = 0
            while (n > 0):
                currDigit = n % 10
                tsum += currDigit ** 2
                n = n // 10
            if tsum == 1:
                return True
            n = tsum
        return False