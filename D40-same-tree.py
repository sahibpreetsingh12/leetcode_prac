"""
Same tree 
Approach:
1. Use a queue to perform a level-order traversal of both trees simultaneously.
2. Start by adding the root nodes of both trees to the queue.
3. While the queue is not empty, pop a pair of nodes (one from each tree) from the queue.
4. If both nodes are None, continue to the next iteration (they match).
5. If one node is None and the other is not, or if their values are different, return False (the trees do not match).
6. If both nodes are not None and their values match, add their left children as a pair to the queue and their right children as a pair to the queue.
7. If the queue is empty and all pairs matched, return True (the trees are the same).

Leetcode Link: https://leetcode.com/problems/same-tree/
"""
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # We will use a queue to process pairs of nodes (one from p, one from q)
        queue = deque()
        # Start by adding the root nodes of both trees
        queue.append((p, q))

        # Process the queue until it's empty
        while queue:
            # Get the next pair of nodes to compare
            n1, n2 = queue.popleft()

            # If both nodes are None, this part of the tree matches, so move on
            if not n1 and not n2:
                continue

            # If one node is None and the other isn't, OR if their values are different
            # the trees are not the same
            elif (not n1 or not n2) or (n1.val != n2.val):
                return False

            else:
                # Both nodes are not None and have the same value
                # Add their left children as a pair to the queue to compare later
                queue.append((n1.left, n2.left))
                # Add their right children as a pair to the queue to compare later
                queue.append((n1.right, n2.right))

        # If we finish processing all node pairs without returning False,
        # it means the trees are the same
        return True
