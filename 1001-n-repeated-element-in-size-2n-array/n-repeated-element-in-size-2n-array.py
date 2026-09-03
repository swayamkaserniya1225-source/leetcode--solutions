class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for  i in range(len(nums)):
            if i+1<len(nums) and nums[i]==nums[i+1]:
                return nums[i]
            if i+2<len(nums) and nums[i]==nums[i+2]:
                return nums[i]
        return nums[0]


        