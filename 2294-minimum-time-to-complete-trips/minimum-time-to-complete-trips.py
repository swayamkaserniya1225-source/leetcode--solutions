class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left=min(time)
        right=left*totalTrips
        while left<=right:
            mid=left+(right-left)//2
            count=0
            for num in time:
                count+=mid//num
            if count>=totalTrips:
                right=mid-1
            else:
                left=mid+1
        return left




        