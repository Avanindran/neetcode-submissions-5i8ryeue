class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        for day, price in enumerate(prices):
            rest = sorted(prices[day:])
            high = max(rest)
            profit = high - price
            if profit > max_profit:
                max_profit = profit

        
        return max_profit


        