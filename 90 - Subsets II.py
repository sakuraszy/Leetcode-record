class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums=sorted(nums)
        def recur(toc,path):
            result.append(path)
            last= None
            for i in range(len(toc)):
                if toc[i]==last:
                    continue
                else:
                    last=toc[i]
                    recur(toc[i+1:],path+[toc[i]])
        recur(nums,[])
        return result