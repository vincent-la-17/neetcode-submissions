class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        count = 1
        maxC = 0
        for i in uniques:
            curr = i
            if i-1 in uniques:
                continue
            else:
                while curr+1 in uniques:
                    count +=1
                    curr +=1
                
                maxC = max(count, maxC)
            count = 1
        return maxC
                