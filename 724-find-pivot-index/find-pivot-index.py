class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=[]
        right=[1]*len(nums)
        prefix=0
        suffix=0
        i=0
        j=len(nums)-1
        while i<len(nums) or j>=0:
            left.append(nums[i]+prefix)
            prefix+=nums[i]
            right[j]=nums[j]+suffix
            suffix+=nums[j]
            i+=1
            j-=1
        for i in range(len(nums)):
            if left[i]==right[i]:
                return i
        return -1
        
