class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        while left<=right:
            mid=left+(right-left)//2
            sum1=0
            for num in nums:
                sum1+=(num//mid)
                if num% mid!=0:
                    sum1+=1
            if sum1<=threshold:
                right=mid-1
            else:
                left=mid+1
        return left

        