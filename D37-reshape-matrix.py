
"""
I n MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

LeetCode Link: https://leetcode.com/problems/reshape-the-matrix/


"""
from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Get the number of rows (l) and columns (b) in the original matrix
        l = len(mat)
        b = len(mat[0])

        # Check if reshaping is possible (total elements must match)
        if l * b == r * c:
            ls = []
            # Flatten the original matrix into a single list
            for i in mat:
                for j in i:
                    ls.append(j)
            
            ks = []
            # Build the new reshaped matrix row by row
            for i in range(0, len(ls), c):
                ks.append(ls[i:i + c])
            
            return ks  # Return the reshaped matrix
        else:
            return mat  # Return the original matrix if reshaping isn't possible

"""
Approach:
1. Get the number of rows (`l`) and columns (`b`) in the original matrix `mat`.
2. Check if reshaping is possible by comparing the total number of elements in the original matrix (`l * b`) with the total number of elements in the desired reshaped matrix (`r * c`).
3. If reshaping is possible, flatten the original matrix into a single list `ls` by iterating through each row and each element.
4. Create a new list `ks` to hold the reshaped matrix.
5. Use a loop to fill `ks` with sublists of size `c` from `ls`, effectively reshaping the matrix.
6. Return the reshaped matrix `ks`.
7. If reshaping is not possible, return the original matrix `mat`.  
"""