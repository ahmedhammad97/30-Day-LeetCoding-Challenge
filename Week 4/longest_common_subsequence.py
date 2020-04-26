from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[None] * (len(text2)+1) for _ in range(len(text1)+1)]
        self.fillGrid(grid, text1, text2)
        return grid[len(text1)][len(text2)]

    
    def fillGrid(self, grid: List[List[int]], text1: str, text2: str):
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i == 0 or j == 0:
                    grid[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    grid[i][j] = grid[i-1][j-1]+1
                else:
                    grid[i][j] = max(grid[i-1][j] , grid[i][j-1])

