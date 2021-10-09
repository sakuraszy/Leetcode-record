class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = list()
        def recur(p,numss):
            if len(numss)==0:
                result.append(p)
            else:
                for i in range(len(numss)):
                    recur(p+[numss[i]],numss[:i]+numss[i+1:])
        recur(list(),nums)
        return result


