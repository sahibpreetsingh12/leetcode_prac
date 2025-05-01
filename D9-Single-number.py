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

Leetcode - https://leetcode.com/problems/single-number/description/
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

        

## New Concept 
## XOR

class Solution(object):
    def singleNumber(self, nums):
        # Initialize a variable to hold the result of XOR operations.
        # We start with 0 because XOR with 0 returns the number itself: 0 ^ a = a
        uniqNum = 0

        # Traverse each number in the list
        for idx in nums:
            # Apply XOR between the current result and the current number.
            # Here's why XOR works for this problem:
            # - XOR of a number with itself is 0 → a ^ a = 0
            # - XOR of a number with 0 is the number itself → a ^ 0 = a
            # - XOR is both commutative and associative, so the order doesn't matter

            # In a list where every number appears exactly twice except one,
            # all the duplicates cancel out: a ^ a = 0
            # What remains is: 0 ^ unique_number = unique_number
            uniqNum ^= idx

        # After the loop, uniqNum will hold the number that appears only once
        return uniqNum
