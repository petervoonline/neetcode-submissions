class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            mid = (lo + hi) // 2 
            row = matrix[mid]
            if target < row[0]:
                hi = mid - 1
            elif target > row[-1]:
                lo = mid + 1
            else:
                for i in row:
                    if i == target:
                        return True 
                return False
        return False 
        