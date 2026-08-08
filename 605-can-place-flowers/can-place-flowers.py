class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower=[0]+flowerbed+[0]
        for i  in range(1,len(flower)-1):
            if flower[i]==0 and  flower[i-1]==0 and flower[i+1]==0:
                flower[i]=1
                n-=1
        return n<=0