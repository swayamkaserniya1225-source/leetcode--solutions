class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        right=sum(nums)
        left=max(nums)
        while left<=right:
            mid=left+(right-left)//2
            count=0
            g=1
            for num in nums:
                count+=num
                if count>mid:
                    count=num
                    g+=1
            if g>k:
                left=mid+1
            else:
                right=mid-1
        return left

                
        
        