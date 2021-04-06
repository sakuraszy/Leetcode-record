class Solution:
    def countAndSay(self, n: int) -> str:
        if n ==1:
            return str(1)
        count =0
        last = None
        r=''
        for i in self.countAndSay(n-1):
            if i==last:
                count +=1
            else:
                if last != None:
                    r+=str(count)
                    r+=str(last)
                last = i
                count =1
        return r+str(count)+str(last)