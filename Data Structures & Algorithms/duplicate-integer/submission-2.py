class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for a in nums:
            if a in seen:
                return True
            seen.add(a)
        return False