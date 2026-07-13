import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap=[]
        for i,data in enumerate(score):
            heapq.heappush(heap,(-data,i))
        list2=[]
        list1=["Gold Medal","Silver Medal","Bronze Medal"]
        for i in range(len(score)):
            x,y=heapq.heappop(heap)
            if i>2:
                score[y]=str(i+1)
            else:
                score[y]=list1[i]
        return score            

        



        