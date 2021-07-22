class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        col=0
        current =1
        result = []
        for i in range(n):
            result.append([0 for x in range(n)])
        while col<=math.ceil(n/2):
            for i in range(col,n-col):
                result[col][i]=current
                current +=1
            for i in range(col+1,n-col-1):
                result[i][n-col-1]=current
                current+=1
            if n-col-1==col:
                break
            for i in range(n-col-1,col-1,-1):
                result[n-col-1][i]=current
                current +=1
            for i in range(n-col-2,col,-1):
                result[i][col]=current
                current +=1
            col+=1
        return result