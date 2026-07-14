"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])
        s = 0
        e = 0
        rooms = 0
        ans=0
        while s < len(intervals):
            if starts[s] <ends[e]:
                rooms+=1
                ans=max(rooms, ans)
                s+=1
            else:
                rooms-=1
                e+=1
        return ans
