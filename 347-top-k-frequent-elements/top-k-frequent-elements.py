import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable=Counter(nums)
        heap=[]
        for  key,value in hashtable.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [points for i,points in heap]