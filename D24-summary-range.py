"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
Leetcode - https://leetcode.com/problems/summary-ranges/
"""
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # If the list is empty, return an empty list
        if not nums:
            return []
        
        ranges: List[str] = []
        start = prev = nums[0]
        
        for n in nums[1:]:
            if n == prev + 1:
                # Still in the current consecutive range
                prev = n
            else:
                # Close out the current range [start…prev]
                if start == prev:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{prev}")
                # Start a new range at n
                start = prev = n
        
        # Append the final range
        if start == prev:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{prev}")
        
        return ranges
