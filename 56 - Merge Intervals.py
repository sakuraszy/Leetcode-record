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

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return intervals
        result=[]
        intervals.sort(key=lambda x:x[0])
        last=intervals[0][0]
        current=intervals[0][1]
        for interval in intervals[1:]:
            if interval[0]>current:
                result.append([last,current])
                last=interval[0]
                current=interval[1]
            else:
                current=max(interval[1],current)
        result.append([last,current])
        return result