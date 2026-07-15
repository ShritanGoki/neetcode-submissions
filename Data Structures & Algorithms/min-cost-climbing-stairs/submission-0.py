class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        
        for n in range(2, len(cost) + 1):
            dp[n] = min(dp[n-1] + cost[n-1], dp[n-2] + cost[n-2])
        
        return dp[len(cost)]

