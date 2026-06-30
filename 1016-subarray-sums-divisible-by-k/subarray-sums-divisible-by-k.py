class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dict1={0:1}
        prefix=0
        count=0
        for num in nums:
            prefix+=num
            if (prefix)%k in dict1:
                count+=dict1[prefix%k]
            dict1[prefix%k]=dict1.get(prefix%k,0)+1
        return count
