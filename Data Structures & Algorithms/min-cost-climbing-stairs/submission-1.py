class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for n in range(len(cost) - 3, -1, -1):
            cost[n] += min(cost[n + 1], cost[n + 2])
        
        return min(cost[0],cost[1])
