class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result=[]
        def recur(s,path):
            if len(path)==4:
                if s=='':
                    result.append('.'.join(path))
                    return
                else:
                    return
            elif len(path)>4 or s =='':
                return
            recur(s[1:],path+[s[0]])
            if s[0] !='0':
                if len(s)>1:
                    recur(s[2:],path+[s[:2]])
                if len(s)>2 and int(s[:3])<=255:
                    recur(s[3:],path+[s[:3]])
        recur(s,[])
        return result