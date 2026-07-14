class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum=0
        max_sum=float("-inf")
        for num in nums:
            currentsum+=num
            max_sum=max(max_sum,currentsum)
            if currentsum<0:
                currentsum=0
        return max_sum

        