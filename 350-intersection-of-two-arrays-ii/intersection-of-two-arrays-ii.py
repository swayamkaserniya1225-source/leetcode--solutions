class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        res=[]
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        for num in nums1:
            dict1[num]=dict1.get(num,0)+1
        for nums in nums2:
            if nums in dict1:
                dict1[nums]-=1
                res.append(nums)
                if dict1[nums]==0:
                    del dict1[nums]
        return res
