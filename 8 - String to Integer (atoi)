class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign =1
        result = 0
        count = 0
        for i in s:
            count +=1
            if count == 1 :
                if i =='-':
                    sign = -1
                elif i=="+":
                    continue
                elif i in '1234567890':
                    result = result*10+int(i)
                else:
                    break
            else:
                if i in '1234567890':
                    result = result*10+int(i)
                else:
                    break
        result = result*sign
        if result > (2**31-1):
            result = (2**31-1)
        elif result < -2**31:
            result = -2**31
        return result