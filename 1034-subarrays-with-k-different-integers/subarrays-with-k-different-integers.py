class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def mostk(k):
            count={}
            array=0
            left=0
            for right in range(len(nums)):
                count[nums[right]]=count.get(nums[right],0)+1
                while len(count)>k:
                    count[nums[left]]-=1
                    if count[nums[left]]==0:
                        del count[nums[left]]
                    left+=1
                array+=right-left+1
            return  array
        return mostk(k)-mostk(k-1)