# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
