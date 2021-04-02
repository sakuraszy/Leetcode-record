class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l= len(needle)
        if needle in haystack:
            for i in range(len(haystack)-l+1):
                #print(haystack[i:i+l])
                if haystack[i:i+l] == needle:
                    return i
            return 0
        else:
            return -1