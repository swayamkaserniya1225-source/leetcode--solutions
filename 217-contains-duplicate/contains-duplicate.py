class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1={}
        for num in nums:
            if num in dict1:
                return True
            dict1[num]=0
        return False
        