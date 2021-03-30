class Solution:
    def intToRoman(self, num: int) -> str:
        trans = {1:'I',4:'IV',9:'IX',40:"XL",5:"V",10:"X",90:"XC",100:"C",500:"D",1000:"M",400:"CD",900:"CM",50:"L"}
        result = ''
        for i in sorted(trans.keys(),reverse=True):
            result += (trans[i]*(num//int(i)))
            num= num%i
        return result