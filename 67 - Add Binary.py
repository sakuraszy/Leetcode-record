class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ad=0
        i=0
        result = ''
        if len(a)>len(b):
            b = '0'*(len(a)-len(b))+b
        else:
            a = '0'*(len(b)-len(a))+a
        i=len(a)-1
        while(i>=0):
            temp = int(a[i])+int(b[i])+ad
            ad=0
            if temp >1:
                temp = temp-2
                ad =1
            result = str(temp)+result
            i-=1
        if ad:
            result = '1'+result
        return result