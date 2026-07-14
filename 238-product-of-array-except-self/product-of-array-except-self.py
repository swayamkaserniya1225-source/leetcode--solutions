class Solution:
    def productExceptSelf(self,nums):
        ans=[1]*len(nums)
        prefix_sum=1
        for i in range(len(nums)):
            ans[i]=prefix_sum
            prefix_sum*=nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans




        