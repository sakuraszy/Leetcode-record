##O(n2)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        l = len(nums)
        result = []
        for i in range(l):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,l):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                right =l-1
                left = 0
                while(right > left):
                    if left ==i or left==j:
                        left +=1
                        continue
                    if right ==i or right==j:
                        right -=1
                        continue
                    temp= nums[i]+nums[j]+nums[left]+nums[right]
                    if temp == target:
                        if sorted ([nums[i],nums[j],nums[left],nums[right]]) not in result:
                            result.append([nums[i],nums[j],nums[left],nums[right]])
                        left +=1
                        right -=1
                    elif temp < target:
                        left+=1
                    else:
                        right-=1
        return result


##recursion

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        def Nsum(num,pre,target,n):
            if n == 2:
                left = 0
                right = len(num)-1
                while(left <right):
                    total = num[left] +num[right]
                    if total == target:
                        r = pre+[num[left],num[right]]
                        if sorted(r) not in result:
                            result.append(r)
                        left+=1
                        right-=1
                    elif total < target:
                        left +=1
                    else:
                        right-=1
            else:
                for i in range(len(num)):
                    if (i==0) or num[i] != num[i-1]:
                        Nsum(num[i+1:],pre+[num[i]],target-num[i],n-1)
        Nsum(nums,[],target,4)
        return result