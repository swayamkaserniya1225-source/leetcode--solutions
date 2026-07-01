class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s1={}
        for right in range(len(nums)):
            if nums[right] in s1:
                if right-s1[nums[right]]<=k:
                    return True
            s1[nums[right]]=right
        return False
            
            