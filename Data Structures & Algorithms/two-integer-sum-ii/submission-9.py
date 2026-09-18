class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while (left < right):
            total = numbers[right] + numbers[left]
            if (total == target):
                return [1+ left, 1+right]
            elif (total > target):
                right -=1
            else:
                left +=1
       
        