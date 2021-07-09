class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxtotal = nums[0]
        lastt = nums[0]
        for i in nums[1:]:
            if lastt <0:
                lastt=i
            else:
                lastt+=i
            print(lastt)
            if lastt>maxtotal:
                maxtotal = lastt
        return maxtotal
                
       