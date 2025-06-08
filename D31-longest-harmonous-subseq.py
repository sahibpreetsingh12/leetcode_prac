"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]

Output: 5

Explanation:

The longest harmonious subsequence is [3,2,2,2,3].

Example 2:

Input: nums = [1,2,3,4]

Output: 2

Explanation:

The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:

Input: nums = [1,1,1,1]

Output: 0

Explanation:

No harmonic subsequence exists.

Leetcode - https://leetcode.com/problems/longest-harmonious-subsequence/
"""
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result = 0
        count_map = {}
        for num in nums:
            if num not in count_map:
                count_map[num] = 1
            else:
                count_map[num] += 1
        for num, count in count_map.items():
            if num + 1 in count_map:
                result = max(count + count_map[num + 1], result)
        return result
"""
# Approach:
1. Initialize a variable `result` to 0 to keep track of the maximum length of harmonious subsequence found.
2. Create a dictionary `count_map` to store the frequency of each number in the input array `nums`.
3. Iterate through each number in `nums`:
   - If the number is not already in `count_map`, add it with a count of 1.
   - If it is already present, increment its count.
4. Iterate through each key-value pair in `count_map`:
   - For each number `num`, check if `num + 1` exists in `count_map`.
   - If it does, calculate the length of the harmonious subsequence formed by `num` and `num + 1` as `count + count_map[num + 1]`.
   - Update `result` to be the maximum of its current value and the calculated length.
5. Finally, return `result`, which contains the length of the longest harmonious subsequence found."""