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
        stack = []
        for i in range(len(intervals)):
            while stack and stack[-1].end <= intervals[i].start:
                stack.pop()
            if stack:
                return False
            stack.append(intervals[i])
        
        return True