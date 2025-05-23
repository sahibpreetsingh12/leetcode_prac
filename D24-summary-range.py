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
"""

Why this works
1. You’re looking for ranges of consecutive integers in a sorted array. 
2. A range is defined as a start and end point, where the end point is the last number in the consecutive sequence.
3. You can iterate through the array and check if the current number is consecutive to the previous one.
4. If it is, you continue; if not, you close out the current range and start a new one.
5. At the end of the iteration, you need to close out the last range.
6. You can use a list to store the ranges in the required format.

Approach
1. Initialize an empty list to store the ranges.
2. If the input list is empty, return an empty list.
3. Set the start and previous variables to the first element of the list.
4. Iterate through the list starting from the second element.   
5. For each element, check if it is consecutive to the previous one.
6. If it is, update the previous variable.
7. If it is not, close out the current range and start a new one.
8. After the loop, close out the last range.
9. Return the list of ranges.
"""
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
