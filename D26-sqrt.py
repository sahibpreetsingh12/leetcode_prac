"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Leetcode - https://leetcode.com/problems/sqrtx/
"""

"""
Why this works
1. You’re looking for the integer square root of a non-negative integer x.
2. The square root of x is the largest integer y such that y * y <= x.
3. You can use binary search to efficiently find the integer square root.
4. Initialize two pointers, left and right, to 1 and x respectively.
5. While left is less than or equal to right, calculate the midpoint.
6. If mid * mid equals x, return mid.
7. If mid * mid is less than x, move the left pointer to mid + 1.
8. If mid * mid is greater than x, move the right pointer to mid - 1.
9. When the loop ends, right is the largest integer where right * right <= x.
10. Return right as the integer square root of x.
"""
from typing import List
class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle edge case: if x is 0, the square root is 0
        if x == 0:
            return 0
        
        # Initialize binary search boundaries
        # left starts at 1 since we handled x = 0, and square root of x >= 1 is at least 1
        # right starts at x since the square root cannot exceed x
        left, right = 1, x
        
        # Perform binary search while left pointer is less than or equal to right
        while left <= right:
            # Calculate the midpoint to avoid integer overflow (instead of (left + right) / 2)
            mid = (left + right) // 2
            
            # Compute the square of mid to compare with x
            square = mid * mid
            
            # If square equals x, mid is the exact square root
            if square == x:
                return mid
            # If square is less than x, the square root is larger, so move left boundary up
            elif square < x:
                left = mid + 1
            # If square is greater than x, the square root is smaller, so move right boundary down
            else:
                right = mid - 1
        
        # When the loop ends, right is the largest integer where right * right <= x
        # This is the floor of the square root of x
        return right