import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l = len(mat)
        b = len(mat[0])

        if l*b == r*c:
            ls=[]
            for i in mat:
                for j in i:
                    ls.append(j)
            

            ks = []
            for i in range(0,len(ls),c):
                ks.append(ls[i:i+c])

            return ks
            
        else:
            return mat
        