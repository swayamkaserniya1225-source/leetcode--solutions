class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        x=None
        if len(nums)==0:
            return [-1,-1]
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                x=mid
                break
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        if x is not None:
            y=x
            while x>=0 and  nums[x]==target:
                x-=1
            while y<len(nums)and  nums[y]==target:
                y+=1
            return [x+1,y-1]
        return[-1,-1]

        