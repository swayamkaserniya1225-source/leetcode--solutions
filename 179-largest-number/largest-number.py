class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def merge_sort(list1):
            if len(list1)>1:
                mid=len(list1)//2
                left=list1[:mid]
                right=list1[mid:]
                merge_sort(left)
                merge_sort(right)
                i=j=k=0
                while i<len(left) and j<len(right):
                    if int(str(left[i])+str(right[j]))>=int(str(right[j])+str(left[i])):
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
        merge_sort(nums)
        return str(int("".join(map(str,nums))))
                