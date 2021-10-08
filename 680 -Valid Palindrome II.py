class Solution:
    def validPalindrome(self, s: str) -> bool:
        def recur(s,deleted):
            if len(s)<2:
                return True
            if s[0]==s[-1]:
                return recur(s[1:-1],deleted)
            else:
                if deleted:
                    return False
                else:
                    return recur(s[:-1],True) or recur(s[1:],True)
        return recur(s,False)
                    