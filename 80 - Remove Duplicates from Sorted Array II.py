class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last =None
        count = 0
        i=0
        while(i<len(nums)):
            if nums[i]==last:
                count +=1
                if count >2:
                    nums.pop(i)
                    i-=1
            else:
                last = nums[i]
                count =1
            i+=1