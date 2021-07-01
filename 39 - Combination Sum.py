class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def recur(pre,candidates,target):
            if target ==0:
                result.append(pre)
                return
            if target <0:
                return
            for i in range(len(candidates)):
                v = candidates[i]
                recur(pre+[v],candidates[i:],target-v)
        recur([],candidates,target)
        return result