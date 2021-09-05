#recursion

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def recur(s,t,start):
            #print(s)
            if start > len(t):
                return 0
            if s==t:
                return 1
            if len(s)<=len(t):
                return 0
            result=0
            for i in range(start,len(s)):
                if s[:i]==t[:i]:
                    result+=recur(s[:i]+s[i+1:],t,i)
            return result
        return recur(s,t,0)