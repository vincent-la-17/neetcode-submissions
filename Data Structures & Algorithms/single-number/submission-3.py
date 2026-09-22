class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniques = set()
        for i in nums:
            if i in uniques:
                uniques.remove(i)
            else:
                uniques.add(i)
        return uniques.pop()