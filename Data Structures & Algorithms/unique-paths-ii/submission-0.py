class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[row-1][col-1]:
            return 0

        dp = [0] * col
        dp[0] = 1

        for r in range(row):
            for c in range(col):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c > 0:
                    dp[c] = dp[c] + dp[c-1]
        
        return dp[col-1]
