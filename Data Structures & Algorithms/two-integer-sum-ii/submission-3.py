class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i,j in enumerate(numbers):
            complement = target-j
            if complement in seen:
                return [seen[complement]+1, i+1]
            seen[j] = i
        return []