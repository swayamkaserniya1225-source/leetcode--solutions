class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        seive=[True]*(n)
        seive[0]=False
        seive[1]=False
        for  i in range(2,int(n**(0.5)+1)):
            if seive[i]:
                for j in range(i*i,n,i):
                    seive[j]=False
        return sum(seive)