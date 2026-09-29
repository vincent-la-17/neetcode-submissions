class Solution:
    def reverse(self, x: int) -> int:
        sgn = x
        rev = int(str(abs(x))[::-1])
        MAX = 2 ** 31 - 1
        MIN = -(2**31)
        if sgn < 0:
            rev = (-1) * rev
        if (rev < MIN) or (rev > MAX):
            return 0

        return rev
