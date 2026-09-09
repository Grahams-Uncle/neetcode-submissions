class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = False 

        up, down = 0, ROWS - 1
        while up <= down:
            mid = (up + down) // 2
            if matrix[mid][0] > target:
                down = mid - 1 
            elif matrix[mid][-1] < target:
                up = mid + 1
            else:
                break
        row = mid

        l, r = 0, COLS - 1
        while l <= r: 
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False 


