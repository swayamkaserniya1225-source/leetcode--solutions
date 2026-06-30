class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=0
        for i in range(len(nums)):
            nums[i]=nums[i]+prefix
            prefix=nums[i]
        return nums
        