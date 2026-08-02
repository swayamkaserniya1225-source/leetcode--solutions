import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def merge_sort(list1):
            if len(list1)>1:
                mid=len(list1)//2
                left=list1[:mid]
                right=list1[mid:]
                merge_sort(left)
                merge_sort(right)
                i=j=k=0
                while i<len(left) and j<len(right):
                    if left[i][1]<right[j][1]:
                        list1[k]=left[i]
                        i+=1
                    else:
                        list1[k]=right[j]
                        j+=1
                    k+=1
                while i<len(left):
                    list1[k]=left[i]
                    i+=1
                    k+=1
                while j<len(right):
                    list1[k]=right[j]
                    j+=1
                    k+=1
        merge_sort(trips)
        heap=[]
        current=0
        for num,start,end in trips:
            while heap and heap[0][0]<=start:
                x,y=heapq.heappop(heap)
                current-=y
            heapq.heappush(heap,(end,num))
            current+=num
            if current>capacity:
                return False
        return True

                



            