import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dist=[[float("inf")]*len(heights[0]) for _ in range(len(heights))]
        dist[0][0]=0
        heap=[]
        heapq.heappush(heap,(0,0,0))
        direction=[(0,-1),(0,1),(1,0),(-1,0)]
        while heap:
            efforts,r,c=heapq.heappop(heap)
            if efforts>dist[r][c]:
                continue
            for dr,dc in direction:
                if 0<=dr+r<len(heights) and 0<=dc+c<len(heights[0]):
                    new_efforts=max(efforts,abs(heights[dr+r][dc+c]-heights[r][c]))
                    if new_efforts<dist[dr+r][dc+c]:
                        dist[dr+r][dc+c]=new_efforts
                        heapq.heappush(heap,(new_efforts,dr+r,dc+c))
        return dist[len(heights)-1][len(heights[0])-1]
                    


        