class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        ml =len(strs[0])
        for i in strs[1:]:
            ml=min(ml,len(i))
        for i in range(ml):
            temp = strs[0][i]
            for x in strs[1:]:
                if x[i] != temp:
                    return strs[0][:i]
        return strs[0][:ml]
    
                