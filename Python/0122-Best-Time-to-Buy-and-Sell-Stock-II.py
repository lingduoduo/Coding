from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        total = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total += prices[i] - prices[i - 1]

        return total


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0)
        return result


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(
                dp[i - 1][0], dp[i - 1][1] - prices[i]
            )  # 注意这里是和121. 买卖股票的最佳时机唯一不同的地方
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[-1][1]
