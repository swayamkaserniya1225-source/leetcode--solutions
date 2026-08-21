class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        prefix=0
        dict1={0:1}
        count=0
        for num  in nums:
            prefix+=num
            if prefix-k in dict1:
                count+=dict1[prefix-k]
            dict1[prefix]=dict1.get(prefix,0)+1
        return count


        