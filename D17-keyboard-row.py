"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Leetcode - https://leetcode.com/problems/keyboard-row/
"""

from typing import List

class Solution:
    def row_finder(self, char: str) -> str:
        if char in "qwertyuiop":
            return "row1"
        elif char in "asdfghjkl":
            return "row2"
        else:
            return "row3"


    def findWords(self, words: List[str]) -> List[str]:
        result = []

        for word in words:
            lowered = word.lower()
            line = self.row_finder(lowered[0])
            
            if all(self.row_finder(c) == line for c in lowered):
                result.append(word)  # use original casing as input

        return result
# Example usage
if __name__ == "__main__":
    sol = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(sol.findWords(words))  # Output: ["Alaska", "Dad"]