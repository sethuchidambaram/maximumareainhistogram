class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        L1=heights
        i=0
        stack=[]
        maxarea = 0
        L1.append(0)
        if not L1:
            return 0
        while i < len(L1) -1:
            stack.append(i)
            if L1[i+1] < L1[i]:
                while stack and L1[stack[-1]] > L1[i+1]:
                    height=stack.pop()
                    leftlimit = 0 if not stack else stack[-1] +1
                    area =L1[height]*(i+1 - leftlimit)
                    if area > maxarea:
                        maxarea = area
            i+=1
        return maxarea    
