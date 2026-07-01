class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        max_freq=0
        left=0
        max1=0
        for  i in range(len(s)):
            count[s[i]]=count.get(s[i],0)+1
            max_freq=max(max_freq,count[s[i]])
            while i-left+1>max_freq+k:
                count[s[left]]-=1
                left+=1
            max1=max(max1,i-left+1)
        return max1
            
                


        