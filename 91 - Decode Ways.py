class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[1]
        dp.append(0 if s[0]=='0' else 1)
        for i in range(2,len(s)+1):
            base =0
            if s[i-1]!='0':
                base= dp[i-1]
            if int(s[i-2:i])>=10 and int(s[i-2:i])<=26:
                dp.append(base+dp[i-2])
            else:
                dp.append(base)
        #print(dp)
        return dp[-1]