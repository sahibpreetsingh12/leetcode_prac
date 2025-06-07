"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
from math import sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Using the formula derived from the quadratic equation
        # k(k + 1) / 2 <= n
        # Rearranging gives us k^2 + k - 2n <= 0
        # We can use the quadratic formula to find k
        return int((-1 + sqrt(1 + 8 * n)) // 2)
# Leetcode - https://leetcode.com/problems/arranging-coins/
"""
from math import sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:
 
        return int(-0.5+sqrt(2*n+0.25))
        
"""
Approach:
1. The problem is about arranging coins in a staircase pattern.
2. The number of complete rows k can be found using the formula derived from the quadratic equation:
   k(k + 1) / 2 <= n
3. Rearranging gives us k^2 + k - 2n <= 0.
4. We can use the quadratic formula to find k:
   k = (-1 + sqrt(1 + 8 * n)) / 2
5. The integer part of k will give us the number of complete rows."""