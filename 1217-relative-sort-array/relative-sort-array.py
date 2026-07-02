class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def merge_sort(list1):
            if len(list1)>1:
                mid=len(list1)//2
                left=list1[:mid]
                right=list1[mid:]
                merge_sort(left)
                merge_sort(right)
                i=j=k=0
                while i<len(left) and j<len(right):
                    if left[i]<right[j]:
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
            return list1
        count1={}
        for num in arr1:
            count1[num]=count1.get(num,0)+1
        i=0
        for num1 in arr2:
            while count1[num1]!=0:
                count1[num1]-=1
                arr1[i]=num1
                i+=1
            del count1[num1]
        k=i
        for key,value in count1.items():
            for _ in range(value):
                arr1[i]=key
                i+=1
        arr1[k:]=merge_sort(arr1[k:])
        return arr1
