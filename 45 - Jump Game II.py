class Solution(object):
    def jump(self, nums):
        if len(nums)<3:
            return len(nums)-1
        far = nums[0]
        current = 0
        step = 0
        for i in range(len(nums)):
            if far < i+nums[i]:
                far = i+nums[i]
            if far >=len(nums)-1:
                return step+1
            if current == i:
                step +=1
                current = far

