class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        while left<=right:
            mid=left+(right-left)//2
            day=1
            load=0
            for num in weights:
                load+=num
                if load>mid:
                    day+=1
                    load=num
            if day<=days:
                right=mid-1
            else:
                left=mid+1
        return left
            
                
            