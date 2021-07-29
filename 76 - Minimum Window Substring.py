class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ''
        maxl=len(s)
        start=0
        end =-1
        toc=list(t)
        for i in t:
            counts[t]+=1
        while start <len(s) or end <len(s)-1:
            if toc !=[] and end <len(s)-1:
                end+=1
                if s[end] in toc:
                    toc.remove(s[end])
            else:
                if end ==len(s)-1 and toc!=[]:
                    break
                if end-start < maxl:
                    result = s[start:end+1]
                    maxl=end-start
                if s[start] not in t:
                    start +=1
                else:
                    temp=list(s[start+1:end+1])
                    for x in t:
                        if x in temp:
                            temp.remove(x)
                        else:
                            toc.append(x)
                            break
                    start +=1
        return result
                