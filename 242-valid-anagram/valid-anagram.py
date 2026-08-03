class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1={}
        for i in range(len(s)):
            dict1[s[i]]=dict1.get(s[i],0)+1
            dict1[t[i]]=dict1.get(t[i],0)-1
        return all(values==0 for values in dict1.values())