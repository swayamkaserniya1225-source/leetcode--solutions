import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap=[]
        for e  in gifts:
            heapq.heappush(heap,-e)
        for i in range(k):
            x=-heapq.heappop(heap)
            x=int(x**0.5)
            heapq.heappush(heap,-x)
        return -sum(heap)


