"""

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize an empty dictionary to count occurrences of each number
        dic_ls = {}

        # Convert the input list to a set to get unique elements
        # Then initialize each unique number's count to 0 in the dictionary
        for i in list(set(nums)):
            dic_ls[i] = 0

        # Loop through the original list and increment the count for each number
        for i in nums:
            if i in dic_ls:
                dic_ls[i] += 1

        # After counting, loop through the dictionary to find the number that occurred exactly once
        for i, j in dic_ls.items():
            if j == 1:
                return i  # This is the number that appears only once

        