class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
        # Update the lowest price seen so far
            if prices[i] < min_price:
                min_price = prices[i]
            else:
            # Check if selling today gives a better profit
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit