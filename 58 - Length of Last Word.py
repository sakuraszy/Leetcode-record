class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t= s.split(" ")
        for x in range(len(t)-1,-1,-1):
            if t[x]!='':
                return len(t[x])
        return 0