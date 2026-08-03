class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1={}
        for right in range(len(nums)):
            if nums[right] in dict1:
                if right-dict1[nums[right]]<=k:
                    return True
            dict1[nums[right]]=right
        return False

        