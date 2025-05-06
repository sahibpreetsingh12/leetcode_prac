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