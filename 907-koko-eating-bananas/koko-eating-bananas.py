class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            total=0
            mid=left+((right-left))//2
            for pile in piles:
                total+=pile//mid
                if pile%mid!=0:
                    total+=1
                if total>h:
                    break
            if total<=h:
                right=mid-1 
            else:
                left=mid+1
        return left