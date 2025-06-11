"""
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].


"""
"""
Approach:
1. Initialize two pointers, `left` and `right`, to represent the search range in the sorted list of characters.
2. Use a binary search to find the smallest character that is lexicographically greater than the target character.
3. If the middle character is greater than the target, move the right pointer to mid; otherwise, move the left pointer to mid + 1.
4. After the loop, use modulo to wrap around the index if necessary, and return the character at the found index.
5. This ensures that if the target is greater than or equal to the largest character in the list, it wraps around to the first character.
"""

from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n  # search range is [left … right)

        # Find the insertion point where ord(letters[mid]) > ord(target)
        while left < right:
            mid = (left + right) // 2
            if ord(letters[mid]) > ord(target):
                right = mid       # mid could be the answer
            else:
                left = mid + 1    # skip mid and anything ≤ target

        # left == 0..n, so wrap around with mod n
        return letters[left % n]