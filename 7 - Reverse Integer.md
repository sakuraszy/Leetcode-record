class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        left = abs(x)
        sign = -1 if x <0 else 1
        while(left !=0):
            result =result*10 +left%10
            left = left//10
        if abs(result) >= 2**31:
            result = 0
        return result*sign