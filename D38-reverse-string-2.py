"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"

"""
# LeetCode Link: https://leetcode.com/problems/reverse-string-ii/
class Solution:
    def logic_bloc(self, k, string_left):
        # If the substring has at least 2k characters
        if len(string_left) >= 2 * k:
            # Reverse the first k characters and keep the next k characters as is
            string_return = string_left[:k][::-1] + string_left[k:2 * k]
            return string_return
        
        # If the substring has at least k but fewer than 2k characters
        elif len(string_left) >= k:
            # Reverse the first k characters and keep the rest as is
            string_return = string_left[:k][::-1] + string_left[k:]
            return string_return
        
        # If the substring has fewer than k characters
        else:
            # Reverse the entire substring
            return string_left[::-1]

    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        
        # Iterate over the string in steps of 2k
        for i in range(0, len(s), 2 * k):
            # Get the next block of up to 2k characters
            string_left = s[i:i + 2 * k]
            
            # Apply logic_bloc to process this block
            part = self.logic_bloc(k, string_left)
            
            # Append the processed part to the result
            result += part
        
        # Return the final transformed string
        return result

"""
Approach:
1. Define a helper method `logic_bloc` that takes an integer `k` and a substring `string_left`. 
2. Inside `logic_bloc`, check the length of `string_left`:
   - If it has at least `2k` characters, reverse the first `k` characters and keep the next `k` characters as is.
   - If it has at least `k` but fewer than `2k` characters, reverse the first `k` characters and keep the rest as is.
   - If it has fewer than `k` characters, reverse the entire substring.
3. In the main method `reverseStr`, initialize an empty string `result`.
4. Iterate over the string `s` in steps of `2k`, extracting substrings of up to `2k` characters.
5. For each substring, call `logic_bloc` to process it and append the result to `result`.
6. Finally, return the transformed string `result`.

"""