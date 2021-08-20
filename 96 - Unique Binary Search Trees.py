class Solution:
    def numTrees(self, n: int) -> int:
        dp=[1,1]
        for i in range(2,n+1):
            temp=0
            for j in range(i):
                temp+=dp[i-j-1]*dp[j]
            dp.append(temp)
        return dp[-1]