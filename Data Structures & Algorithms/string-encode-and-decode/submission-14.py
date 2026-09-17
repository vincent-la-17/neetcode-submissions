class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for a in strs:
            result += str(len(a)) + "#" + a
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
      
        while i < len(s):
            j = i
            while (s[j] != "#"):
                j = j+1
            length = int(s[i:j])
            i = j + 1
            result.append(s[i:i+length])
            i = i+length
        return result

