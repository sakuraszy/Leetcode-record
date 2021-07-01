class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result= list()
        nums= sorted(nums)
        def recur(p,ns):
            if ns==[]:
                result.append(p)
            else:
                for i in range(len(ns)):
                    if i== 0 or ns[i] !=ns[i-1]:
                        recur(p+[ns[i]],ns[:i]+ns[i+1:]) 
        recur([],nums)
        return result