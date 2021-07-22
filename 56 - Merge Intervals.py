class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        start=intervals[0][0]
        laste = intervals[0][1]
        if len(intervals)<=1:
            return intervals
        for inter in intervals[1:]:
            if inter[0] <= laste:
                laste = max(inter[1],laste)
            else:
                result.append([start,laste])
                start = inter[0]
                laste = inter[1]
        result.append([start,laste])
        return result