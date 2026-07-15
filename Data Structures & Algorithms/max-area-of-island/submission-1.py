class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if (not 0<=r<rows or not 0<=c<cols
                or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r+1, c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(dfs(r,c), maxArea)
        
        return maxArea
