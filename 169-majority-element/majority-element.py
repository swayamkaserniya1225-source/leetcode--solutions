class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element=None
        count=0
        for num in nums:
            if count==0:
                element=num
            if element==num:
                count+=1
            else:
                if count>0:
                    count-=1
        return element            
        