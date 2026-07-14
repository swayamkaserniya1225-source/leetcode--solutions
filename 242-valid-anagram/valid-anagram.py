class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashtable=[0]*26
        for i in range(len(s)):
            index=ord(s[i])-ord("a")
            hashtable[index]+=1
            index1=ord((t[i]))-ord("a")
            hashtable[index1]-=1
        return hashtable==[0]*26