"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        longest = min(strs, key=len)  # Use the shortest word for prefix bounds
        ls = []

        for i in range(len(longest)):
            temp_char = longest[i]
            counter = 0  # Reset counter at the start of each character position

            for j in strs:
                if j[i] == temp_char:
                    counter += 1
                else:
                    break

            if counter == len(strs):
                ls.append(temp_char)
            else:
                break

        return ''.join(ls)
