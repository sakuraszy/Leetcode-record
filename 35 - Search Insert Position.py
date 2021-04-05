class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        result =0
        mid = 0
        while(start <= end):
            mid = (start+end)//2
            if nums[mid]>target:
                result= mid
                end = mid-1
            elif nums[mid]< target:
                start=mid+1
                result= mid+1
            else:
                result = mid
                break
        return result