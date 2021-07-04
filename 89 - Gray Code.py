class Solution:
    def grayCode(self, n: int) -> List[int]:
        def conver(numl):
            result= []
            for s in numl:
                l=len(s)
                r= 0
                for i in range(l-1,-1,-1):
                    r+= 2**(l-i-1)*int(s[i])
                result.append(r)
            return result
        def recur(n):
            if n==1:
                return(['0','1'])
            temp = recur(n-1)
            temp2 = temp.copy()
            temp2.reverse()
            for i in range(len(temp2)):
                temp2[i] = '1'+temp2[i]
            for i in range(len(temp)):
                temp[i]='0'+temp[i]
            #print(temp+temp2)
            return temp + temp2
        return conver(recur(n))