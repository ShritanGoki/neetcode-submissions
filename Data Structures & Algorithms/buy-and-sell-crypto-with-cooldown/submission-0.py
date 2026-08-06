class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        rest = 0
        sold = 0

        for p in prices[1:]:
            prevHold, prevRest, prevSold = hold, rest, sold

            hold = max(prevHold, prevRest - p)
            sold = prevHold + p
            rest = max(prevRest, prevSold)
        

        return max(rest, sold)



            

