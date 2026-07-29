class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for v in range(1, amount + 1):
                if (v-c) >= 0:
                    dp[v] += dp[v-c]
        
        return dp[amount]


        