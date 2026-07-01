class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first=0
        s1=set()
        max2=0
        for i in range(0,len(s)):
            while s[i] in s1:
                s1.remove(s[first])
                first+=1
            max2=max(max2,i-first+1) 
            s1.add(s[i])
        return max2
            




            