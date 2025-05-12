"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

Leetcode - https://leetcode.com/problems/group-anagrams/

"""
from typing import List
# Explanation: Grouping anagrams is a common problem in coding interviews and competitive programming.
# The idea is to use a hashmap (or dictionary) to group words that are anagrams of each other.
# An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.
# For example, "eat", "tea", and "ate" are anagrams because they contain the same letters in different orders.
#
# Approach:
# 1. Use a hashmap to store lists of words that are anagrams of each other.
# 2. The key for the hashmap will be the sorted version of the word, which will be the same for all anagrams.
# 3. Iterate through each word in the input list, sort it, and use it as a key to group the words.
# 4. Finally, return the values of the hashmap as a list of lists, where each inner list contains anagrams.
#
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a hashmap (defaultdict) to group anagrams.
        # The key will be the sorted version of each word, the value will be a list of words (anagrams).
        ana_map = defaultdict(list)
        
        # Iterate through each string in the input list.
        for i in strs:
            # Sort the characters in the string to get a common key for anagrams.
            # Example: "eat" -> "aet", "tea" -> "aet", so they will be grouped together.
            sorted_s = ''.join(sorted(i))  # Sorting takes O(k log k), where k is length of the string.
            
            # Append the original string to the list of its anagram group in the map.
            ana_map[sorted_s].append(i)
        
        # Collect all anagram groups from the hashmap and return as the final result.
        return list(ana_map.values())

