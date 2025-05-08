"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2: 

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Leetcode -  https://leetcode.com/problems/4sum/
"""
class Solution:         
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        # Skip duplicate first elements
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Skip duplicate second elements
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                    
                # Use two pointers for the remaining two elements
                left = j + 1
                right = n - 1
                
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if curr_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                        
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
                        
        return result
"""
solution which didnt work -- Its correct but not efficient for time

from itertools import combinations
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        nums.sort()  # Sort to group duplicates
        result = set()  # Use set to avoid duplicates
        
        for quad in combinations(nums, 4):
            if sum(quad) == target:
                result.add(quad)  # Add tuple to set (tuples are hashable)
        
        return [list(quad) for quad in result]

        
"""