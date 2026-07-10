class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        left=min(bloomDay)
        right=max(bloomDay)
        while left<=right:
            mid=left+(right-left)//2
            count=0
            bouque=0
            for day in  bloomDay:
                if day<=mid:
                    count+=1
                else:
                    count=0
                if count==k:
                    bouque+=1
                    if bouque>=m:
                        break
                    count=0
            if bouque<m:
                left=mid+1
            else:
                right=mid-1
        return left
            

                
        