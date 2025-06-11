"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Output: "leetcode"
Example 2:
Input: s = "abBAcC"
Output: ""
Output: ""
Example 3:
Input: s = "s"
Output: "s"

LeetCode Link: https://leetcode.com/problems/make-the-string-great/

"""
from typing import List
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
"""
Approach:
1. Initialize an empty stack to keep track of characters.
2. Iterate through each character in the string `s`.
3. For each character, check if the stack is not empty and if the absolute difference between the ASCII values of the last character in the stack and the current character is 32 (indicating they are the same letter but in different cases).
4. If the condition is met, pop the last character from the stack (removing the adjacent bad pair).
5. If the condition is not met, append the current character to the stack.
6. Finally, return the joined characters in the stack as the resulting good string.
"""
