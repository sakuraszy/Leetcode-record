class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        result = 0
        for i in range(len(s)):
            if(s[i] in s[start:i]):
                result = max(result,i-start)
                while (s[start] != s[i]):
                    start +=1
                start +=1
        result = max(result,len(s)-start)
        return result