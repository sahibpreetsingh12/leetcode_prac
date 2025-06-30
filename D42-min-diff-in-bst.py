"""
Approach:
1. Define a `TreeNode` class to represent each node in the binary search tree (BST).
2. Define a `Solution` class with a method `getMinimumDifference` that takes the root of the BST as input.
3. Use a helper function `collect` to traverse the tree and collect all node values in a list.
4. Sort the collected values to prepare for finding the minimum absolute difference.
5. Initialize a variable `min_diff` to infinity to keep track of the minimum difference found.
6. Iterate through the sorted values and calculate the absolute difference between each pair of consecutive values.
# 7. Update `min_diff` if the current difference is smaller than the previously recorded minimum.
7. Return the smallest absolute difference found.
LeetCode Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Helper function to collect all node values from the tree
        def collect(node, values):
            if node:
                values.append(node.val)           # Add the current node's value
                collect(node.left, values)        # Recurse on the left subtree
                collect(node.right, values)       # Recurse on the right subtree

        values = []
        collect(root, values)                     # Step 1: Collect all node values (in any order)

        values.sort()                             # Step 2: Sort the values to compare adjacent ones

        min_diff = float('inf')                   # Initialize minimum difference as infinity
        for i in range(1, len(values)):           # Step 3: Compare adjacent values
            diff = abs(values[i] - values[i-1])   # Absolute difference between consecutive elements
            min_diff = min(min_diff, diff)        # Update min_diff if current diff is smaller

        return min_diff                           # Return the smallest absolute difference found
