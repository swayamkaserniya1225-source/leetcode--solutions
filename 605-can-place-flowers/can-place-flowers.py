class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        if len(flowerbed)==1:
            if flowerbed[0]==0 and n<=1:
                return True
            elif flowerbed[0]==1 and n==0:
                return True
            else:
                return False
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if i-1>=0 and i+1<len(flowerbed) and flowerbed[i-1]==flowerbed[i+1]==0:
                    count+=1
                    flowerbed[i]=1
                elif i-1<0 and i+1<len(flowerbed) and flowerbed[i+1]==0:
                    count+=1
                    flowerbed[i]=1
                elif i>0 and i+1==len(flowerbed) and flowerbed[i-1]==0:
                    count+=1
                if count>=n:
                    return True
        return False
        

        