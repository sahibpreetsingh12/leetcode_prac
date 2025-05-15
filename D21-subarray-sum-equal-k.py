"""

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Leetcode - https://leetcode.com/problems/subarray-sum-equals-k/
"""

# brute force solution
"""
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        subarrays = []
        n = len(nums)
        for i in range(n):          # start index
            for j in range(i, n):   # end index
                # A[i:j+1] is the subarray from i through j
                if sum(nums[i:j+1])==k: 
                    subarrays.append(nums[i:j+1])
        return len(subarrays)
"""

# Optimized solution
# The optimized solution uses a hashmap to store the prefix sums and their counts.
# The prefix sum is the sum of all elements from the start of the array to the current index.
# The idea is to keep track of how many times each prefix sum has occurred.
# If the difference between the current prefix sum and k has been seen before, it means there is a subarray that sums to k. 
# We can then increment the count of subarrays found.   
# # This approach has a time complexity of O(n) and a space complexity of O(n).
# # Approach:
# 1. Initialize a hashmap to store the prefix sums and their counts.
# 2. Initialize a variable to keep track of the current prefix sum.
# 3. Initialize a variable to keep track of the number of subarrays found.
# 4. Iterate through the array:
#    - Update the current prefix sum by adding the current element.
#    - Check if the difference between the current prefix sum and k has been seen before.
#      - If it has, increment the count of subarrays found by the count of that prefix sum.
#    - Update the hashmap with the current prefix sum.   
from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Map from prefix-sum value → how many times we've seen it so far
        count = defaultdict(int)
        count[0] = 1        # “empty” prefix before we start

        cur = 0             # running prefix sum
        result = 0

        for x in nums:
            cur += x
            # Any prior prefix sum = cur-k gives a subarray summing to k ending here
            result += count[cur - k]
            # Record this prefix sum for future matches
            count[cur] += 1

        return result
