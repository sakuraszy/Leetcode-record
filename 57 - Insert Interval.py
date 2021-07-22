class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        for inter in range(len(intervals)):
            if intervals[inter][1]< newInterval[0]:
                continue
            else:
                if newInterval[1]<intervals[inter][0]:
                    intervals.insert(inter,newInterval)
                    return intervals
                start = min(intervals[inter][0],newInterval[0])
                end = max(newInterval[1],intervals[inter][1])
                count = inter+1
                while(count<len(intervals)):
                    if intervals[count][0]>end:
                        break
                    else:
                        end=max(intervals[count][1],end)
                        intervals.pop(count)
                intervals[inter][0]=start
                intervals[inter][1]=end
                return intervals
        intervals.append(newInterval)
        return intervals