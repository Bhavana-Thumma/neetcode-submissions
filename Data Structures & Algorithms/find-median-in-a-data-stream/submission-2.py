from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.data=SortedList()

    def addNum(self, num: int) -> None:
        # bisect.insort(self.data, num)
        self.data.add(num)

    def findMedian(self) -> float:
        n = len(self.data)
        mid = n//2
        if(n%2 == 1):
            return self.data[mid]
            
        else:
            return (self.data[mid-1]+self.data[mid])/2
        
        