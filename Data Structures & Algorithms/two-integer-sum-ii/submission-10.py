class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while (left <= right):
            curr = numbers[right] + numbers[left]   
            if curr == target:
                return [left+1, right+1]
            elif curr > target:
                right -= 1
            elif curr < target:
                left +=1 
        return [left+1, right+1]