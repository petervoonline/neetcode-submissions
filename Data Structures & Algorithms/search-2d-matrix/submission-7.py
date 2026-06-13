class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1
        mid = 0
        # Binary Search matrix to see if target is within the range of any row
        while lo <= hi:
            mid = (lo + hi) // 2 
            row = matrix[mid]
            if target < row[0]:
                hi = mid - 1
            elif target > row[-1]:
                lo = mid + 1
            else:
                break

        # Binary Search Row if target is within range of a specific row, else target is not within matrix
        if (lo > hi):
            return False
        row = matrix[mid]
        lo = 0
        hi = len(row) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if target < row[mid]:
                hi = mid - 1
            elif target > row[mid]:
                lo = mid + 1
            else:
                return True
            
        
        return False 
        