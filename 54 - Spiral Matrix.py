class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cols=len(matrix)
        rows=len(matrix[0])
        c=0
        r=0
        result = []
        while (c<math.ceil(cols/2) and r<math.ceil(rows/2)):
            for i in range(r,rows-r):
                result.append(matrix[c][i])
            for i in range(c+1,cols-c):
                result.append(matrix[i][rows-r-1])
            if cols%2 ==1 and c+1==math.ceil(cols/2):
                break
            for i in range(rows-r-2,r-1,-1):
                result.append(matrix[cols-c-1][i])
            if rows%2 ==1 and r+1==math.ceil(rows/2):
                break
            for i in range(cols-c-2,c,-1):
                result.append(matrix[i][r])
            #print(result)
            c+=1
            r+=1
        return result
                
  