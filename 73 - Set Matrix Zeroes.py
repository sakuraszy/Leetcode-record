class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        ml=[]
        nl=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    ml.append(i)
                    nl.append(j)
        for i in set(ml):
            for j in range(n):
                matrix[i][j]=0
        for j in set(nl):
            for i in range(m):
                matrix[i][j]=0