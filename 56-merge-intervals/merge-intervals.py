class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def merge_sort(list1):
            if len(list1)>1:
                mid=len(list1)//2
                left=list1[:mid]
                right=list1[mid:]
                merge_sort(left)
                merge_sort(right)
                i=j=k=0
                while i<len(left) and j<len(right):
                    if left[i][0]<=right[j][0]:
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
        merge_sort(intervals)
        i=0
        res=[]
        while i<len(intervals):
            j=i+1
            while j<len(intervals)and(intervals[j][0]<=intervals[i][1]):
                intervals[i]=[intervals[i][0],max(intervals[j][1],intervals[i][1])]
                j+=1
            res.append(intervals[i]) 
            i=j
        return res