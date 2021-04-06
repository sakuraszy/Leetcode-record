class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        candidates.sort()
        def recur(path,c,target):
            if target ==0:
                result.append(path)
                return 
            if target <0:
                return
            if c == []:
                return 
            last = None
            for i in range(len(c)):
                v = c[i]
                if v != last:
                    recur(path+[v],c[i+1:],target-v)
                    last = v
                else:
                    continue
        recur([],candidates,target)
        return result