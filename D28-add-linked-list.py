"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Leetcode - https://leetcode.com/problems/add-two-numbers/
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, 
        l1: Optional[ListNode], 
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Dummy head to simplify code (we’ll return dummy.next at the end)
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        p, q = l1, l2
        while p is not None or q is not None or carry != 0:
            # If one list is exhausted, use 0 as its digit
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            
            total = x + y + carry
            digit = total % 10
            carry = total // 10
            
            # Append the new digit node
            current.next = ListNode(digit)
            current = current.next
            
            # Advance pointers if possible
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        
        return dummy.next
