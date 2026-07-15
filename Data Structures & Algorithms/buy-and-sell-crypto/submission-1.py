class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minCost = prices[0]

        for num in prices:
            profit = max(profit, num-minCost)
            minCost = min(minCost, num)
        return profit