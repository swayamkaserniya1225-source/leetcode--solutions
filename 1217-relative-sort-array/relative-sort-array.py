class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
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
        arr1[k:]=sorted(arr1[k:])
        return arr1
