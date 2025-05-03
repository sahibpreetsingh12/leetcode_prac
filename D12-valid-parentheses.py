"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 
leetcode -  https://leetcode.com/problems/valid-parentheses/description/
"""

"""
Approach -1 (Counting) - Not Solving all test cases

class Solution:
    def isValid(self, s: str) -> bool:
        para_count={"(":0,")":0,"{":0,"}":0,"[":0,"]":0}
        for i in range(len(s)):
            if s[i]=="(":
                para_count["("]+=1
            elif s[i]==")":
                para_count[")"]+=1
            elif s[i]=="{":
                para_count["{"]+=1
            elif s[i]=="}":
                para_count["}"]+=1
            elif s[i]=="[":
                para_count["["]+=1
            elif s[i]=="]":
                para_count["]"]+=1
        

        if (para_count["("]==para_count[")"]) and (para_count["{"]==para_count["}"]) and (para_count["["]==para_count["]"]):
            return True
        else:
            return False
        
"""