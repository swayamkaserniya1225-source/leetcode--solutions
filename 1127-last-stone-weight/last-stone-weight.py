import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for e in stones:
            heapq.heappush(heap,-e)
        while len(heap)>1:
            root=heapq.heappop(heap)
            x=heapq.heappop(heap)
            val=root-x
            if val<0:
                heapq.heappush(heap,val)
        if heap:
            return -heap[0]
        return 0

            

        