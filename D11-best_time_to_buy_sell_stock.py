"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

leetcode -  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
"""
Intuition

1. You’re tracking the cheapest day to buy (min_price) as you move through the array.

2. On each day, you check how much profit you’d make if you sold today, using that cheapest buy day.

3. You update the max profit accordingly.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to the first day's price
        # This will track the lowest price we've seen so far
        min_price = prices[0]

        # Initialize profit to 0 (no transaction yet)
        profit = 0

        # Iterate through the list of prices
        for i in range(len(prices)):
            # Calculate potential profit if we sold on the current day
            margin = prices[i] - min_price

            # If we find a new lower price, update min_price (as if we found a better day to buy)
             
            if prices[i] < min_price:
                min_price = prices[i]

            # Update max profit if current margin is higher
            # (as if we found a better day to sell)
            if margin > profit:
                profit = margin

        # Return the maximum profit found during the loop
        return profit
    

# Not Optimised Approach

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_margin = 0  # Initialize max profit

        # Loop through each day to choose as a potential buy day
        for i in range(len(prices) - 1):
            buy_price = prices[i]

            # Check the maximum price in the remaining days (possible sell prices)
            # This involves slicing and using max, which takes O(n) time per iteration
            sell_price = max(prices[i + 1:])

            # Calculate profit margin if we bought on day i and sold on the best future day
            margin = sell_price - buy_price

            # Update max_margin if this profit is higher
            if margin > max_margin:
                max_margin = margin

        return max_margin

"""