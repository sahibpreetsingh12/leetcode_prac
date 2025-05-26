"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Leetcode - https://leetcode.com/problems/missing-number/

"""
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Calculate the sum of all numbers in the input array
        sum1 = sum(nums)
        
        # Create a range from 0 to n (length of nums + 1) and compute its sum
        # This represents the expected sum if no number was missing
        sum2 = sum([i for i in range(len(nums)+1)])
        
        # The missing number is the difference between the expected sum (sum2) and actual sum (sum1)
        return sum2 - sum1
    