class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        current=0
        wl=[]
        result = []
        for i in range(len(words)):
            if i != len(words) and current +len(words[i])<= maxWidth:
                current +=(len(words[i])+1)
                wl.append(words[i])
            else:
                if len(wl)==1:
                    result.append(wl[0]+' '*(maxWidth-len(wl[0])))
                    wl=[words[i]]
                else:
                    temp=''
                    extra= (maxWidth-current+1)//(len(wl)-1)
                    leftover = (maxWidth-current+1)%(len(wl)-1)
                    for w in wl[:-1]:
                        temp+=w
                        temp+=' '*(extra+1+(1 if leftover>0 else 0))
                        leftover -=1
                    temp+=wl[-1]
                    result.append(temp)
                wl = [words[i]]
                current =len(words[i])+1
        lastline= ' '.join(wl)
        result.append(lastline+' '*(maxWidth-len(lastline)))
        return result