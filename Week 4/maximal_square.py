from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] and i and j:
                    # All prev cells
                    top = matrix[i-1][j]
                    left = matrix[i][j-1]
                    topLeft = matrix[i-1][j-1]
                    matrix[i][j] = min(top, left, topLeft) + 1
        # Checks that the matrix is not empty first
        return len(matrix) and max(map(max, matrix)) ** 2

