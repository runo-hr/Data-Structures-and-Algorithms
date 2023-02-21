# You are given an array prices where prices[i] is the price of a 
# given stock on the ith day.

# You want to maximize your profit by choosing a single day 
# to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

class Solution:
    def max_profit(self, prices):
        '''
        prices: array
        return profit
        '''
        l,r = 0,1 # buy and sell indices
        profit = 0 # initial profit
        while r < len(prices):
            if prices[r] > prices[l]: # profitable
                profit = max(profit, prices[r] - prices[l])
            else: # lower buying price
                l = r
            r += 1
        return profit