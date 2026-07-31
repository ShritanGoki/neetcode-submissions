"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        for i in range(1, len(intervals)):
            interval2 = intervals[i]
            interval1 = intervals[i-1]

            if interval1.end > interval2.start:
                return False
            
        return True