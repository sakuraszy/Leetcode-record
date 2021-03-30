class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result= []
        def recur(pre,leftn,rightn,n):
            if leftn==n:
                while(rightn != leftn):
                    pre+=')'
                    rightn+=1
                result.append(pre)
                return
            else:
                if leftn>rightn:
                    recur(pre+'(',leftn+1,rightn,n)
                    recur(pre+')',leftn,rightn+1,n)
                elif leftn==rightn:
                    recur(pre+"(",leftn+1,rightn,n)
                else:
                    return
        recur('',0,0,n)
        return result