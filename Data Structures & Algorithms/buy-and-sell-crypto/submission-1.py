class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        profit = 0

        for i, price in enumerate(prices[0: len(prices) - 1]):
            max_profit = max(prices[i + 1:]) - price 
            profit = max(max_profit, profit)
        

        return profit