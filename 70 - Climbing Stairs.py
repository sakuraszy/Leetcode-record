class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[]
        for i in range(n+1):
            if i<3:
                dp.append(i)
            else:
                dp.append(dp[i-1]+dp[i-2])
        return dp[-1]