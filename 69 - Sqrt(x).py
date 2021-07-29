class Solution:
    def mySqrt(self, x: int) -> int:
        last=0
        if x <2:
            return x
        right = x//2
        left = 2
        while(left<=right):
            num = left+(right-left)//2
            #print(num,left)
            if num*num<x:
                left = num+1
            elif num*num==x:
                return num
            else:
                right = num-1
        return right