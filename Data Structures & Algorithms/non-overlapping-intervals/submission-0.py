#Greedy Algorithm
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prevEnd = intervals[0][1]
        remove = 0
        for start,end in intervals[1:]:
            if start>=prevEnd:
                prevEnd = end
            else:
                remove+=1
                prevEnd = min(prevEnd, end)
        return remove

        