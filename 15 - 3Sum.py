class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        last = None
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            if nums[i]==last:
                continue
            while (left< right):
                temp = nums[left]+nums[right]+nums[i]
                if temp==0:
                    if sorted([nums[left],nums[right],nums[i]]) not in result:
                        result.append(sorted([nums[left],nums[right],nums[i]]))
                    left+=1
                    right-=1
                elif temp<0:
                    left +=1
                else:
                    right -=1
            last = nums[i]
        return result