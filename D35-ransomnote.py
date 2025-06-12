"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
LeetCode Link: https://leetcode.com/problems/ransom-note/
"""
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter      = Counter(ransomNote)
        magazine_counter    = Counter(magazine)
        return ransom_counter == ransom_counter & magazine_counter
  
        
        return True
    
"""
Approach:
1. Use the `Counter` class from the `collections` module to count the occurrences of each character in both `ransomNote` and `magazine`.
2. Compare the character counts of `ransomNote` and `magazine` using the bitwise AND operator (`&`).
3. If the character counts of `ransomNote` are equal to the character counts of `ransomNote` AND `magazine`, it means that all characters needed for `ransomNote` are present in `magazine`.
4. If the condition is met, return `True`, indicating that `ransomNote` can be constructed from `magazine`.
5. If the condition is not met, return `False`, indicating that `ransomNote` cannot be constructed from `magazine`.
"""