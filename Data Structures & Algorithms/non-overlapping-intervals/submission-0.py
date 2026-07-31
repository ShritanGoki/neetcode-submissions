class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEndTime = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] >= prevEndTime:
                prevEndTime = interval[1]
            else:
                res += 1
                prevEndTime = min(prevEndTime, interval[1])
        
        return res
