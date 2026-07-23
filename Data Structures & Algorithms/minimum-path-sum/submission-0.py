class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [0] * len(grid[0])
        dp[0] = grid[0][0]
        for i in range(1, len(grid[0])):
            dp[i] = dp[i-1] + grid[0][i]
            
        for r in range (1, len(grid)):
            dp[0] += grid[r][0]
            for c in range(1, len(grid[0])):
                dp[c] = min(dp[c-1],dp[c]) + grid[r][c]
        

        return dp[len(grid[0])-1]

        