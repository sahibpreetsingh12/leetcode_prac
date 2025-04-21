"""
Given two integer arrays nums1 and nums2, 
return an array of their intersection. 
Each element in the result must appear as many times 
as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            map_list = nums1
            big_map = nums2
        elif len(nums1) > len(nums2):
            map_list = nums2
            big_map = nums1
        else:
            # When both lists are of equal size, 
            #choose arbitrarily or raise an error
            # Here, we default to choosing nums1 as the small list
            map_list = nums1
            big_map = nums2

        temp_ls=[]
        for i in map_list:
            if i in big_map:
                temp_ls.append(i)
                big_map.remove(i)
        return temp_ls