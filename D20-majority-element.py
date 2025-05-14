"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
Leetcode - https://leetcode.com/problems/majority-element/

"""
from typing import List
# Explanation: The problem is asking for the majority element in an array, which is the element that appears more than n/2 times.
# The Boyer-Moore Voting Algorithm is an efficient way to find the majority element in linear time and constant space.
# The algorithm works by maintaining a count of the current candidate for the majority element and adjusting it based on the elements in the array.
# The key idea is that if the count drops to zero, we pick a new candidate.
# This works because the majority element appears more than half the time, so it will always be the last candidate standing.
# Approach:

# 1. Initialize a candidate variable and a count variable.
# 2. Iterate through the array:
#    - If the count is zero, set the current element as the candidate and set count to 1.
#    - If the current element is the same as the candidate, increment the count.
#    - If the current element is different, decrement the count.
# 3. After iterating through the array, the candidate will be the majority element.             
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapper = defaultdict(int)
        n = len(nums)
        
        for num in nums:
            mapper[num] += 1
            if mapper[num] > n // 2:
                return num
        
        # Since the problem guarantees a majority element, this line is technically unreachable
        return 0