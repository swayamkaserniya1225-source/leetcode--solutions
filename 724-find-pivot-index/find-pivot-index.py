class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=[]
        prefix=0
        for i in range(len(nums)):
            left.append(nums[i]+prefix)
            prefix+=nums[i]
        right=[1]*len(nums)
        prefix=0
        for j in range (len(nums)-1,-1,-1):
            right[j]=nums[j]+prefix
            prefix+=nums[j]
        for i in range(len(nums)):
            if left[i]==right[i]:
                return i
        return -1
        
