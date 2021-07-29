class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        coln=-1
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                if i==0:
                    return False
                else:
                    coln = i-1
                    break
        left =0
        right = len(matrix[coln])-1
        while(left <=right):
            mid= (left+right)//2
            if matrix[coln][mid]==target:
                return True
            elif (matrix[coln][mid] >target):
                right-=1
            else:
                left+=1          
                
                
        return False