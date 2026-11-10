class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        cache[0] = 0
        cache[1] = 1
        cache[2] = 2
        for i in range(3,n+1):
            cache[i] = cache[i-2] + cache[i-1]
        return cache[n]

        
            
            
        