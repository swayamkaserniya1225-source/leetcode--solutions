class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for  i in range(len(nums)):
            nums[i]=(nums[i])**2
        def mergesort(nums):
            if len(nums)>1:
                mid=len(nums)//2
                left=nums[:mid]
                right=nums[mid:]
                mergesort(left)
                mergesort(right)
                i=j=k=0
                while i<len(left) and j<len(right):
                    if left[i]<right[j]:
                        nums[k]=left[i]
                        i+=1
                    else:
                        nums[k]=right[j]
                        j+=1
                    k+=1
                while  i<len(left):
                    nums[k]=left[i]
                    i+=1
                    k+=1
                while j<len(right):
                    nums[k]=right[j]
                    j+=1
                    k+=1
            return nums
        return mergesort(nums)

        