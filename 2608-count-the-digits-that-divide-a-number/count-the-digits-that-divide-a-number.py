class Solution:
    def countDigits(self, num: int) -> int:
        t=num
        count=0
        while t>9:
            if num%(t%10)==0:
                count+=1
            t//=10
        if num%t==0:
            return count+1
        return count
        