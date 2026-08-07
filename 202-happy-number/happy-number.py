class Solution:
    def isHappy(self, n: int) -> bool:
        s1=set()
        def helper(n):
            s=0
            while n:
                s+=((n%10)**2)
                n//=10
            if s in s1:
                return False
            elif s==1:
                return True
            s1.add(s)
            return helper(s)
        return helper(n)
