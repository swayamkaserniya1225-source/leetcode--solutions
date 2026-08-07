class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s1=set()
        for i  in range (len(nums)):
            for j in  range (2,int((nums[i])**0.5)+1):
                if nums[i]%j==0:
                    s1.add(j)
                    while nums[i]%j==0:
                        nums[i]//=j
            if nums[i]>1:
                s1.add(nums[i])
        return len(s1)

            
            