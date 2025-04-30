

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

https://leetcode.com/problems/pascals-triangle/
"""
from typing import List

"""
My own solution
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the final result list which will hold all rows of Pascal's Triangle
        big_ls = []

        # Loop through each row index from 1 to numRows (inclusive)
        for i in range(1, numRows + 1):
            # Start every row with 'i' elements initialized to 1
            # In Pascal's Triangle, the first and last elements of each row are always 1
            row = [1] * i

            # Fill in the values between the first and last element for rows beyond the second
            for j in range(1, i - 1):
                # Compute the value based on the sum of two values from the previous row
                # Specifically, row[j] = previous_row[j] + previous_row[j-1]
                # We use i-2 because 'big_ls' is 0-indexed and we're currently at row 'i'
                row[j] = big_ls[i - 2][j] + big_ls[i - 2][j - 1]

            # Append the completed row to the result list
            big_ls.append(row)

        # Return the list of lists containing Pascal's Triangle up to numRows
        return big_ls

        
# class Solution:
#     # recurssion solution
#     def generate(self, numRows: int) -> List[List[int]]:
#         if numRows == 0:
#             return []
#         if numRows == 1:
#             return [[1]]
        
#         prevRows = self.generate(numRows - 1)
#         newRow = [1] * numRows
        
#         for i in range(1, numRows - 1):
#             newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
        
#         prevRows.append(newRow)
#         return prevRows


"""
Simpler Solution - we need to work on recurrsion before moving further
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle