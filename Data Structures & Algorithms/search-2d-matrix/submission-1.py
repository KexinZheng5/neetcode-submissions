class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)
        tr = 0

        while l < r:
            tr = (l + r) // 2
            if matrix[tr][0] > target:
                r = tr
            elif matrix[tr][-1] < target:
                l = tr + 1
            else:
                break
        
        l = 0
        r = len(matrix[0])
        while l < r:
            m = (l + r) // 2
            if matrix[tr][m] == target:
                return True
            elif matrix[tr][m] < target:
                l = m + 1
            else:
                r = m

        return False