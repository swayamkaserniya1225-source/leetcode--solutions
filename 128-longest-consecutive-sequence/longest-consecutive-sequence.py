class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_dist=0
        nums1=set(nums)
        for  i in range(len(nums)):
            num=nums[i]
            if (num-1) not in nums1:
                count=0
                while num in nums1:
                    count+=1
                    num+=1
                max_dist=max(count,max_dist)
            if max_dist>=len(nums1):
                return max_dist
        return max_dist


        