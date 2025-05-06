"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""

# Approach we have to think of is 2 pointer

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Initialize two pointers: one at the start and one at the end of the list
        left, right = 0, len(s) - 1
        
        # Loop until the two pointers meet in the middle
        while left < right:  # This was the key part you were missing: the two-pointer approach
            
            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]
            
            # Move the left pointer forward
            left += 1
            
            # Move the right pointer backward
            right -= 1
