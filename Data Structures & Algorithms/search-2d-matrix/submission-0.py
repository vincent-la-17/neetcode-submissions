class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(row, target):
            left = 0
            right = len(row)-1
            
            while left <= right:
                mid = (left + right)//2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        for i in matrix:
            if binarySearch(i, target):
                return True
        return False