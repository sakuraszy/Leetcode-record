class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ml = len(matrix)
        l = len(matrix)/2
        for i in range(l+ml%2):
            for j in range(l):
                temp = matrix[ml-j-1][i]
                matrix[ml-j-1][i]=matrix[ml-i-1][ml-j-1]
                matrix[ml-i-1][ml-j-1]=matrix[j][ml-i-1]
                matrix[j][ml-i-1]=matrix[i][j]
                matrix[i][j]= temp
            
                    