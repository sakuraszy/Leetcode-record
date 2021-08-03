class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def recur(nums,path):
            result.append(path)
            for i in range(len(nums)):
                recur(nums[i+1:],path+[nums[i]])
        recur(nums,[])
        return result