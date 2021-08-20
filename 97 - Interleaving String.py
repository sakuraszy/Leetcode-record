class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp=[]
        if len(s1)+len(s2) != len(s3):
            return False
        for i in range(len(s1)+1):
            dp.append([True for x in range(len(s2)+1)])
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j !=0:
                    dp[i][j]=(dp[i][j-1] and (s3[i+j-1])==s2[j-1])
                elif j==0 and i !=0:
                    dp[i][j]=(dp[i-1][j] and (s3[i+j-1])==s1[i-1])
                elif i !=0 and j!= 0:
                    dp[i][j]=(dp[i][j-1] and (s3[i+j-1])==s2[j-1]) or (dp[i-1][j] and (s3[i+j-1])==s1[i-1])
        #print(dp)
        return dp[-1][-1]