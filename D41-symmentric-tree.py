from collections import deque
from typing import Optional
# LeetCode Link: https://leetcode.com/problems/symmetric-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # An empty tree is symmetric
        if not root:
            return True
        
        # Initialize a queue that will store pairs of nodes to compare
        queue = deque()
        # Start by comparing the left and right children of the root
        queue.append((root.left, root.right))
        
        while queue:
            # Take the next pair of nodes to compare
            # popleft() removes and returns the first pair from the queue
            t1, t2 = queue.popleft()
            
            # If both nodes are None, this part of the tree is symmetric so far; move on to next pair
            if not t1 and not t2:
                continue
            
            # If only one of the nodes is None, the structure is asymmetric
            if not t1 or not t2:
                return False
            
            # If the values of the two nodes are different, the tree is not symmetric
            if t1.val != t2.val:
                return False
            
            # If the nodes are valid and equal, add their children to the queue in mirrored order
            # This ensures we always compare nodes that should be mirror images:
            # - left child of t1 with right child of t2
            # - right child of t1 with left child of t2
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        
        # If we've checked all pairs and found no asymmetry, the tree is symmetric
        return True


"""
Approach:
1. Check if the root is None. If it is, return True since an empty tree is symmetric.
2. Initialize a queue to hold pairs of nodes to compare.
3. Start by adding the left and right children of the root to the queue.
4. While the queue is not empty, pop a pair of nodes from the queue.
5. If both nodes are None, continue to the next iteration (they match).
6. If one node is None and the other is not, return False (the tree is not symmetric).
7. If both nodes are not None and their values match, add their left child of the first node and the right child of the second node as a pair to the queue, and vice versa for the right child of the first node and the left child of the second node.
8. If the queue is empty and all pairs matched, return True (the tree is symmetric).
"""