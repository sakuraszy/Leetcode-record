class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = None
        minu = 0
        for i in range(len(nums)):
            if last == nums[i-minu]:
                nums.pop(i-minu)
                minu+=1
            last = nums[i-minu]
        return len(nums)
        