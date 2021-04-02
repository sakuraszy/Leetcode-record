class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows==1):
            return s
        step =1
        result = list()
        current = 0
        for i in range(numRows):
            result.append(list())
        for c in s:
            result[current].append(c)
            current += step
            if current ==0:
                step = 1
            elif current == (numRows-1):
                step= -1
        final =''
        for ele in result:
            final += ''.join(ele)
        return final