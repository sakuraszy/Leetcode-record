class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        minu =0
        for i in range(len(nums)):
            if nums[i-minu] == val:
                nums.pop(i-minu)
                minu +=1
        return len(nums)