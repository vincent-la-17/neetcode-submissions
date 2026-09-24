class Solution:
    def reverseBits(self, n: int) -> int:
        result = ""
        for i in range(32):
            result = result + str((n >> i) & 1) 
        
        return int(result,2)
