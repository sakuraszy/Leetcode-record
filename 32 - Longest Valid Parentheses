class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        result =0
        brea = -1
        for index,i in enumerate(s):
            if i=='(':
                left +=1
            else:
                right +=1
            if left ==right:
                result = max(result,index-brea)
            if right > left:
                right= 0
                left = 0
                brea = index
        left = 0
        right = 0
        brea = len(s)         
        for i in range(len(s)-1,-1,-1):
            print(i)
            if s[i]=='(':
                left +=1
            else:
                right +=1
            if left ==right:
                result = max(result,brea-i)
            if right < left:
                right= 0
                left = 0
                brea = i
            #@print(result)
        return result
                