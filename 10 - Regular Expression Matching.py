#version 1
```python

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p =='':
            return s==''
        elif s != '':
            if (len(p)>1 and p[1] =='*'):
                if p[0]=='.':
                    if len(p)==2:
                        return True
                    else:
                        return self.isMatch(s[1:],p) or self.isMatch(s,p[2:])
                else:
                    if(s[0]==p[0]):
                        return self.isMatch(s[1:],p) or self.isMatch(s,p[2:])
                    else:
                        return self.isMatch(s,p[2:])
            if(p[0]=='.'):
                return self.isMatch(s[1:],p[1:])
            elif(p[0]==s[0]):
                return self.isMatch(s[1:],p[1:])
            else:
                return False
        else:
            if(len(p)>1 and p[1] =='*'):
                return self.isMatch(s,p[2:])


```


# version 2 DP