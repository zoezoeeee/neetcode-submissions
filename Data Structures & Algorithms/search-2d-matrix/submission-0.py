class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, m * n - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            row = mid // n
            col = mid % n
            cur = matrix[row][col]

            if cur == target:
                return True
            elif cur > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False