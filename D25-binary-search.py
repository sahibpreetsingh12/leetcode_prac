"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Leetcode - https://leetcode.com/problems/search-insert-position/
"""
"""
Why this works
1. You’re looking for the position of a target value in a sorted array.
2. If the target is found, return its index.
3. If the target is not found, return the index where it would be if it were inserted in order.
4. You can use binary search to efficiently find the target or the insertion point.
5. Initialize two pointers, start and end, to the beginning and end of the array.
6. While start is less than or equal to end, calculate the midpoint.
7. If the target is equal to the midpoint value, return the midpoint index.
8. If the target is less than the midpoint value, move the end pointer to mid - 1.
9. If the target is greater than the midpoint value, move the start pointer to mid + 1.
10. If the target is not found, return the start pointer, which will be the insertion point.

Now How start pointer is actually the insertion point when element is not found?
1. The start pointer represents the first index where the target could be inserted while maintaining the sorted order.
2. If the target is less than the value at the midpoint, it means the target should be inserted before the midpoint.
3. If the target is greater than the value at the midpoint, it means the target should be inserted after the midpoint.
4. When the loop ends, the start pointer will be at the correct insertion point.
Let's take an example:
1. nums = [1, 3, 5, 6], target = 2
2. start = 0, end = 3
3. mid = (0 + 3) // 2 = 1, nums[mid] = 3
4. Since target (2) < nums[mid] (3), we move end to mid - 1 = 0
5. Now start = 0, end = 0
6. mid = (0 + 0) // 2 = 0, nums[mid] = 1
7. Since target (2) > nums[mid] (1), we move start to mid + 1 = 1
8. Now start = 1, end = 0
9. The loop ends because start (1) > end (0)    
10. The start pointer (1) is the correct insertion point for target (2) in the sorted array [1, 3, 5, 6].

"""

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2  # Calculate midpoint based on current range
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:  # target > nums[mid]
                start = mid + 1
        
        return start  # Return the insertion point