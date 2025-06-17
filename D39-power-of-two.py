
"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
Approach:
    1. Check if `n` is less than or equal to 0. If it is, return `False` since negative numbers and zero cannot be powers of two.
    2. Use the `math.log2` function to calculate the base-2 logarithm of `n`.
    """
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        t = math.log2(n)
        return t.is_integer()
    
#without Math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n // 2
        return n == 1
"""
Approach:
1. Check if `n` is less than or equal to 0. If it is, return `False` since negative numbers and zero cannot be powers of two.
2. Use a while loop to repeatedly divide `n` by 2 as long as `n` is even (i.e., `n % 2 == 0`).
3. After the loop, check if `n` is equal to 1. If it is, return `True`, indicating that `n` is a power of two.
4. If `n` is not equal to 1, return `False`, indicating that `n` is not a power of two.
"""
