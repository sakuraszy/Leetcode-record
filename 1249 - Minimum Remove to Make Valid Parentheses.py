class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result=''
        stack=[]
        count=0
        for i,character in enumerate(s):
            if character=="(":
                stack.append(i)
            elif character==')':
                if len(stack)>0:
                    stack.pop(-1)
                else:
                    s=s[:i-count]+s[i+1-count:]
                    count +=1
        for i in stack:
            s=s[:i-count]+s[i+1-count:]
            count +=1
        return s