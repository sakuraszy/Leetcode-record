class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        maxi = nums[0]
        for i in range(len(nums)):
            if i>maxi:
                return False
            temp=i+nums[i]
            if temp > maxi:
                maxi =temp
            if maxi >= len(nums)-1:
                return True
        return False
                