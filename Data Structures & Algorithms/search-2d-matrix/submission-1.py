class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix)-1
        while row_l <= row_r:
            row_m = (row_l+row_r)//2
            col_l, col_r = 0, len(matrix[row_m])-1
            if target < matrix[row_m][col_l]:
                row_r = row_m - 1 
                continue

            elif target > matrix[row_m][col_r]:
                row_l = row_m + 1

            else:
                while col_l <= col_r:
                    col_m = (col_l+col_r)//2

                    if matrix[row_m][col_m] == target:
                        return True
                    elif matrix[row_m][col_m] > target:
                        col_r = col_m - 1
                    else:
                        col_l = col_m  + 1

                return False

        return False 