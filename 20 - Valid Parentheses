class Solution:
    def isValid(self, s: str) -> bool:
        rec = list()
        check = {"}":"{",']':'[',')':'('}
        for i in s:
            if i in '{[(':
                rec.append(i)
            elif i in ')]}':
                if len(rec)>0 and check[i] == rec[-1]:
                    rec.pop()
                else:
                    return False
        return len(rec)==0