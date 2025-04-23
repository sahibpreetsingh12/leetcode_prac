"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false

https://leetcode.com/problems/monotonic-array/
"""


from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        We have taken sorted arrays
        both ascending and descending sorted because monotinic can be anything
        """
        return True if sorted(nums)==nums or sorted(nums,reverse=True)==nums else False

        