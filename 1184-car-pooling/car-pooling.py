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
        prefix=0
        dict1={}
        for num,start,end in trips:
            prefix=num
            dict1[start]=dict1.get(start,0)+prefix
            dict1[end]=dict1.get(end,0)-prefix
        current=0
        for i in range(0,1000):
            current+=dict1.get(i,0)
            if current>capacity:
                return False
        return True


                



            