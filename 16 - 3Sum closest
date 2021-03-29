class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = sum(nums[:3])
        nums = sorted(nums)
        l = len(nums)-1
        for i,v in enumerate(nums):
            if i>0 and nums[i-1]==v:
                continue
            left =i+1
            right = l
            while(left<right):
                if left ==i:
                    left+=1
                elif right ==i:
                    right -=1
                else:
                    #print(v,nums[left],nums[right])
                    temp = v+nums[left]+nums[right]
                    if abs(temp-target)< abs(result-target):
                        result = temp
                    if temp >target:
                        right -=1
                    elif temp<= target:
                        left+=1
        return result