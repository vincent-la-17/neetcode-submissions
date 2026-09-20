class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
     
        for i in range(len(nums)):
            curr = nums[i]
            left = i+1
            right = len(nums)-1
           
            while left < right:
                target = curr + nums[left] + nums[right]
                if target > 0:
                    right -= 1
                elif target <0:
                    left += 1
                else:
                    if ([curr, nums[left], nums[right]]) not in res:
                        res.append([curr, nums[left], nums[right]])
                    left +=1
                    right -=1
      
        return res

