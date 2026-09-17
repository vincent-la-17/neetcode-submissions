class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tracker = set(nums)
        max_length = 0
       
        curr_length = 0
        curr_val = 0
        i = 0
        for x in tracker:
            if (x-1) not in tracker:
                curr_length = 1
                while x+1 in tracker:
                    curr_length +=1
                    x = x+1
                    max_length = max(max_length,curr_length)
            
        return max(max_length,curr_length)
                