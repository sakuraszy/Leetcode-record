class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend>0) == (divisor<0):
            sign = -1
        if abs(divisor)==1:
            return max(min(abs(dividend)*sign,2**31-1),-2**31)
        dividend =abs(dividend)
        divisor = abs(divisor)
        result = 0
        while( dividend >= divisor):
            temppower = 1
            tempv = divisor
            while(dividend >= tempv+tempv):
                tempv+=tempv
                temppower += temppower
            result += temppower
            dividend-=tempv
        return max(min(result*sign,2**31-1),-2**31)