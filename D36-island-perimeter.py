"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


LeetCode Link: https://leetcode.com/problems/island-perimeter/

"""
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Get the number of rows in the grid
        length = len(grid)

        # Get the number of columns in the grid
        breadth = len(grid[0])

        # Initialize perimeter counter
        perimeter = 0

        # Iterate over each cell in the grid
        for i in range(length):
            for j in range(breadth):
                # Check if the current cell is land (1)
                if grid[i][j] == 1:
                    # Start with 4 sides for each land cell
                    perimeter += 4

                    # Check for adjacent land cell above and subtract 1 if present
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 1

                    # Check for adjacent land cell below and subtract 1 if present
                    if i < length - 1 and grid[i+1][j] == 1:
                        perimeter -= 1

                    # Check for adjacent land cell to the left and subtract 1 if present
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 1

                    # Check for adjacent land cell to the right and subtract 1 if present
                    if j < breadth - 1 and grid[i][j+1] == 1:
                        perimeter -= 1
                else:
                    # If water, continue to next cell
                    continue

        # Return the total calculated perimeter
        return perimeter
# Example usage:
# grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[0,0,0,0]]
# solution = Solution()
# print(solution.islandPerimeter(grid))  # Output: 16
# LeetCode Link: https://leetcode.com/problems/island-perimeter/


"""
Approach:
1. Get the number of rows and columns in the grid.
2. Initialize a variable `perimeter` to keep track of the total perimeter.
3. Iterate through each cell in the grid using nested loops.    
4. For each cell, check if it is land (1). If it is:
   - Start with a perimeter of 4 for that cell.
   - Check the adjacent cells (up, down, left, right) to see if they are also land (1).
   - If an adjacent cell is land, subtract 1 from the perimeter for each adjacent land cell found.
5. If the cell is water (0), continue to the next cell.
6. After iterating through all cells, return the total perimeter calculated.
"""