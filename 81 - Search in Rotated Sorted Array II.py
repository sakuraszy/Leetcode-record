class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i=0
        if len(nums)==1:
            return target==nums[0]
        if target >=nums[0]:
            while(i< len(nums)-1 and nums[i]<=nums[i+1] and target>=nums[i]):
                if nums[i]==target:
                    return True
                i+=1
            return nums[i]==target
        else:
            i=len(nums)-1
            while(i>0 and nums[i-1]<=nums[i] and target <= nums[i]):
                if nums[i]==target:
                    return True
                i-=1
            return nums[i]==target