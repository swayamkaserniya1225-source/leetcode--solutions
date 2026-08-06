class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        seive=[True]*(n+1)
        seive[0]=False
        seive[1]=False
        for  i in range(2,int(n**(0.5)+1)):
            j=2
            if seive[i]:
                for j in range(i*i,n,i):
                    seive[j]=False
        count=0
        for i in range(n):
            if seive[i]:
                count+=1
        return count