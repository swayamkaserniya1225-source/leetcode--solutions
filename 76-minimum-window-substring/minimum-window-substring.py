class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        hash1={}
        minimum=float("inf")
        x=0
        need =len(t)
        for ch in t:
            hash1[ch]=hash1.get(ch,0)+1
        left=0
        for right in range(len(s)):
            if s[right] in hash1:
                hash1[s[right]]-=1
                if hash1[s[right]]>=0:
                    need-=1
            while need==0 and left<len(s):
                if right-left+1<minimum:
                    minimum=right-left+1
                    x=left
                if s[left] in hash1:
                    hash1[s[left]]+=1
                    if hash1[s[left]]>0:
                        need+=1
                left+=1
        if minimum==float("inf"):
            return ""
        return s[x:x+minimum]

        


            