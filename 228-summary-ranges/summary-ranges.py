class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        list1=[]
        i=0
        while i<len(nums):
            j=nums[i]
            while i+1<len(nums) and nums[i]+1==nums[i+1]:
                i+=1
            if j==nums[i]:
                list1.append(str(nums[i]))
            else:
                list1.append(f"{j}->{nums[i]}")
            i+=1
        return list1


