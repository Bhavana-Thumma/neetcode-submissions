class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        for i in range(len(heights)):
            j = len(heights) -1
            while(j>=i+1):
                w = min(heights[j], heights[i]) * (j-i)
                m =max(m, w)
                j-=1
        return m
            
        