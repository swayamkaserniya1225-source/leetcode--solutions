class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x=1
        y=0
        while n>9:
            x*=(n%10)
            y+=(n%10)
            n//=10
        return (x*n)-(y+n)


            
        