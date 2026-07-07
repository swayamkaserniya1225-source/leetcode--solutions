class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findbound(nums):
            left=0
            right=len(nums)-1
            x=-1
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]==target:
                    x=mid
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return x
        def findlast(nums):
            left=0
            right=len(nums)-1
            x=-1
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]==target:
                    x=mid
                    left=mid+1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return x
        return [findbound(nums),findlast(nums)]


        