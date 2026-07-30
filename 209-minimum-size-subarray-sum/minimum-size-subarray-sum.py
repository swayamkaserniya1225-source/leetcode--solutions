class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        size=float("inf")
        sum1=0
        for right  in range(len(nums)):
            sum1+=nums[right]
            while  sum1>=target:
                size=min(size,right-left+1)
                sum1-=nums[left]
                left+=1
        if size!=float("inf"):
            return size
        return 0

            
                

        