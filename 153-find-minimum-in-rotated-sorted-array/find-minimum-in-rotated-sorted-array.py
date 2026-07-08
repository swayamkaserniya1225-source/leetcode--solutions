class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        min1=float("inf")
        left=0
        right=len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            # if nums[left]<nums[mid]:
            #     min1=min(min1,nums[left])
            #     left=mid+1
            if nums[right]<nums[mid]:
              left=mid+1
            else:
                right=mid
        return nums[left]
        