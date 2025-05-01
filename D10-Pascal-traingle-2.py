"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]


leetcode - https://leetcode.com/problems/pascals-triangle-ii/description/
"""

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
                
        numRows=rowIndex+1
        big_ls = []

        
        for i in range(1, numRows + 1):
            
            row = [1] * i

            
            for j in range(1, i - 1):
                
                row[j] = big_ls[i - 2][j] + big_ls[i - 2][j - 1]

            
            big_ls.append(row)

        
        return big_ls[-1]
        