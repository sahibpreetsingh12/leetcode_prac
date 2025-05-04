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
Concepts learned

"""
class Solution:
    def isValid(self, s: str) -> bool:
        pop_stack = []  # Stack to keep track of opening brackets

        # Quick check: if length is odd, it can't be valid (each open must have a close)
        if len(s) % 2 != 0:
            return False

        # Iterate through each character in the string
        for i in range(len(s)):
            temp = 0  # Temp variable (optional, not really needed)

            # If current char is an opening bracket, push it to stack
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                pop_stack.append(s[i])
                continue

            # If a closing bracket is found and stack is empty, no matching open bracket
            elif len(pop_stack) == 0:
                return False

            # Check if the current closing bracket matches the top of the stack
            elif s[i] == ")" and pop_stack[-1] == "(":
                temp = pop_stack.pop()  # Valid match, pop the opening bracket

            elif s[i] == "]" and pop_stack[-1] == "[":
                temp = pop_stack.pop()

            elif s[i] == "}" and pop_stack[-1] == "{":
                temp = pop_stack.pop()

            # If it's a closing bracket but doesn't match the stack top, invalid
            else:
                return False

        # After processing all characters, if stack is empty → all brackets matched
        if len(pop_stack) != 0:
            return False
        else:
            return True

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