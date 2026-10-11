class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
        
    def decode(self, s: str) -> List[str]:
        i = 0
        
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            currLength=int(s[i:j])
            #j is at the #
            i = j+1
            #moved to the first after #
            res.append(s[i:i+currLength])
            #moved to after word
            i = i+currLength

        return res
