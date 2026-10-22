class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [element for row in matrix for element in row]
        left = 0
        right = len(flat)-1
        while left <= right:
            mid =  (left+right)//2
            if flat[mid] == target:
                return True
            elif flat[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return False