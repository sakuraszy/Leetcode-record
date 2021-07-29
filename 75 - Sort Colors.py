class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        current =0
        i=0
        last = len(nums)-1
        while(nums[last]==2 and last >0):
            last-=1
        while (i<len(nums) and i <= last):
            if nums[i]==0:
                nums.pop(i)              
                nums.insert(0,0)
                i+=1
            elif nums[i]==2:
                nums.pop(i)
                nums.append(2)
                last-=1
            else:
                i+=1
        if nums[-1]==0:
            nums.pop(-1)
            nums.insert(0,0)
            