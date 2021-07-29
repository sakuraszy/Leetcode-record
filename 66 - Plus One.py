class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]=str(int(digits[-1])+1)
        count = 0
        for i in range(len(digits)-1,-1,-1):
            digits[i]=str(int(digits[i])+count)
            count=0
            if digits[i]=='10':
                digits[i]='0'
                count=1
            else:
                break
            #print(digits)
        if count ==1:
            digits=['1']+digits
        return digits