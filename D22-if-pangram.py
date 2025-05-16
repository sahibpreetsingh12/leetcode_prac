"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false

Leetcode - https://leetcode.com/problems/check-if-the-sentence-is-pangram/
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        #step-1 and 2 at a time as we are doing AUSCII stuff
        c=97
        
        for i in range(26):
            if chr(c) not in sentence:
                return False
                break
            else:
                c+=1
        return True

        