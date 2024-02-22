"""
215. Best time to buy and sell stock with transaction fee
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Given bunch of stock prices and ability to buy/sell multiple times, find out maximum profit achievable.

Final algorithm followed:
1. Maintain 2 arrays for when you buy the ith stock/sell the ith stock.
2. Compute max profit until day i given you sold stock on i or you bought stock on i.
3. Return max profit overall.

Summary of common mistakes/tricks:
When you qualify for multiple actions, think of creating arrays for each action.
"""
# Solution with comments
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # The idea is to have 2 arrays that maintain max profits if we buy the stock and if we sell the stock at each timestep.
        # We should also account for doing nothing on a given day.
        hold, free = [0] * len(prices), [0] * len(prices)
        # if we bought the 1st stock, we'd have paid the price for it
        hold[0] = -prices[0]

        for i in range(1, len(prices)):
            # account for doing nothing by looking at 1 timestep behind and taking max
            hold[i] = max(hold[i-1], free[i-1]-prices[i])
            free[i] = max(free[i-1], hold[i-1]+prices[i]-fee)
    
        return max(hold[-1], free[-1])