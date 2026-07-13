class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        result = []
        for interval in intervals:
            start,end = interval
            if not result:
                result.append(interval)
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append(interval)
        return result