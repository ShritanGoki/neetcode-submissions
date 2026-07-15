class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuy = prices[0]

        for price in prices:
            minBuy = min(minBuy, price)
            profit = max(profit, price - minBuy)

        return profit