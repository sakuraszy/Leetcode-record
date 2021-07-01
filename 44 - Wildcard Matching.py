class Solution(object):
    def isMatch(self, s, p):
        dp=[]
        for x in range(len(p)+1):
            dp.append([1 for x in range(len(s)+1)])
        dp[0][0]= True
        for i in range(len(s)+1):
            for j in range(len(p)+1):
                if j==0:
                    if i!=0:
                        dp[j][i]=False
                elif i==0:
                    if j !=0:
                        dp[j][i] = dp[j-1][i] and p[j-1]=="*"
                else:
                    if p[j-1]=='?':
                        dp[j][i]= dp[j-1][i-1]
                    elif p[j-1]=="*":
                        dp[j][i]= dp[j-1][i-1]or dp[j-1][i]or dp[j][i-1]
                    else:
                        dp[j][i]= dp[j-1][i-1] and s[i-1]==p[j-1]
        #print(dp)
        return dp[-1][-1]
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        