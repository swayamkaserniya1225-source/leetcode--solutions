class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum1={0:-1}
        x=0
        max1=0
        for i  in range(len(nums)):
            if nums[i]==1:
                x+=1
            else:
                x-=1
            if x in sum1:
                max1=max(i-sum1[x],max1)
            else:
                sum1[x]=i
        return max1

            



        