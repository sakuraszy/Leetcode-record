class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i ==0 and j==0:
                    obstacleGrid[i][j] = 0 if obstacleGrid[i][j]==1 else 1
                elif i==0 and j !=0:
                    obstacleGrid[i][j]= 0 if obstacleGrid[i][j-1]==0 or obstacleGrid[i][j]==1 else 1
                elif i!=0 and j==0:
                    obstacleGrid[i][j]= 0 if obstacleGrid[i-1][j]==0 or obstacleGrid[i][j]==1 else 1
                else:
                    if obstacleGrid[i][j]==0:
                        obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                    else:
                        obstacleGrid[i][j]=0
                #print(obstacleGrid)
        return obstacleGrid[-1][-1]