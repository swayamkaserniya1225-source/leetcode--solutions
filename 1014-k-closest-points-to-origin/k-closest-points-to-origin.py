class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for  i ,data  in enumerate(points):
            square=data[0]**2+data[1]**2 
            heapq.heappush(heap,(square,i)) 
        l1=[] 
        for i in range(k):
            x,y=heapq.heappop(heap)
            l1.append(points[y])
        return l1