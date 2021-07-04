class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for x in strs:
            result[tuple(sorted(list(x)))].append(x)
        return result.values()