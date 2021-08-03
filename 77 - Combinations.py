class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        opt = [i for i in range(1,n+1)]
        def recur(opt,k,path):
            if k==0:
                result.append(path)
            else:
                for i in range(len(opt)):
                    recur(opt[i+1:],k-1,path+[opt[i]])
        recur(opt,k,[])
        return result