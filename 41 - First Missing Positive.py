class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
        nums.sort()
        flag = False
        for i in range(len(nums)-1):
            if (nums[i]>0) and not flag:
                if nums[i] >1:
                    return 1
                flag = True
            if flag:
                if i==0 and nums[i]> 1:
                    return 1
                else:
                    if nums[i+1]-nums[i]>1:
                        return nums[i]+1
        if flag:
            return nums[-1]+1
        else:
            if nums[-1]==1 :
                return 2
            else:
                return 1


////////

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing =1
        for i in nums:
            if i ==missing:
                missing +=1
        return missing


/////

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        if nums ==[1]:
            return 2
        for i in range(len(nums)):
            if nums[i]<=0 or nums[i]>=(len(nums)+1):
                nums[i]=1
        for i in nums:
            i = abs(i)
            if nums[i-1]>0:
                nums[i-1] = -nums[i-1]
        for i in range(len(nums)):
            if nums[i]>0:
                return i+1
        return len(nums)+1
            