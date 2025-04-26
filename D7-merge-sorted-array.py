"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. To accommodate this, nums1 has a 
length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined 
elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only 
there to ensure the merge result can fit in nums1.

https://leetcode.com/problems/merge-sorted-array/
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        Since we have to do inplace operation so 
        Steps below:-
        1. Take the first m elements from nums1 (the actual numbers we care about, ignoring the extra zeros at the end).
        2. Combine these m elements with all the elements from nums2 to make a new temporary list.
        3. Sort this temporary list so all numbers are in order (smallest to largest).
        4. Copy the sorted numbers back into nums1, replacing everything in nums1 with these sorted numbers.
        5. Check if there are any zeros in nums1 that shouldn’t be there and remove them (this step is only needed for some edge cases).
        """
        # Step 1 & 2: Take first m elements of nums1 and combine with nums2
        t = nums1[:len(nums1)-n] + nums2
        # Step 3: Sort the combined list
        t.sort()
        # Step 4: Copy sorted elements back to nums1
        for i in range(len(t)):
            nums1[i] = t[i]
        # Step 5: Remove any unwanted zeros (this handles edge cases like negative numbers)
        for i, j in zip(nums1, range(len(nums1)-1)):
            if (i == 0) and (nums1[j+1] < 0):
                nums1.remove(0)

s = Solution()
print(s.merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))