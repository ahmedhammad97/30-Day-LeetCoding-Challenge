from typing import List

# First Attempt: Time limit exceeded
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.recursivePathSum(grid, [0, 0])
    
    
    def recursivePathSum(self, grid: List[List[int]], pos: List[int]) -> int:
        if self.isGoalCell(pos, grid):
            return grid[pos[0]][pos[1]] 
    
        down_min_sum = right_min_sum = None
        if self.isInsideGrid([pos[0] + 1, pos[1]], grid):
            down_min_sum = self.recursivePathSum(grid, [pos[0] + 1, pos[1]])
        else:
            down_min_sum = 2**31
            
        if self.isInsideGrid([pos[0], pos[1] + 1], grid):
            right_min_sum = self.recursivePathSum(grid, [pos[0], pos[1] + 1])
        else:
            right_min_sum = 2**31
        
        return grid[pos[0]][pos[1]] + min(down_min_sum, right_min_sum)
    
    
    def isGoalCell(self, pos: List[int], grid: List[List[int]]) -> bool:
        return pos == [len(grid) - 1, len(grid[0]) - 1]
    
    
    def isInsideGrid(self, pos: List[int], grid: List[List[int]]) -> bool:
        return pos[0] < len(grid) and pos[1] < len(grid[0])


# I realized the simple recurrence `curr_min = curr_val + min(down_min, right_min)`,
# So all I needed was two recursice calls to the down and right cells
# But it turns out to be too slow.


##########################################################################


# Second Attempt: Accepted
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cost = [[0]*len(grid[0]) for _ in range(len(grid))]
        cost[0][0] = grid[0][0]

        # Fill first row
        for j in range(1,len(grid[0])):
            cost[0][j] = grid[0][j] + cost[0][j-1]
        
        # Fill first column
        for i in range(1,len(grid)):
            cost[i][0] = grid[i][0] + cost[i-1][0]
        
        # Fill rest of the cost matrix
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]
        
        return cost[len(grid)-1][len(grid[0])-1]


# Instead of doing recursive calls, we can memoize the cost at every cell
# in a cost matrix, at the end of this procedure, the minimum cost to reach
# the target cell would be the same recurrence: `curr_val + min(down_min, right_min)`,
# But now, down_min, and right_min are static values in the cost matrix.