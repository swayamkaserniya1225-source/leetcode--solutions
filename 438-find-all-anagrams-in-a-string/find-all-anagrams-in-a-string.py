class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict1={}
        arr=[]
        count=0
        for num in p:
            dict1[num]=dict1.get(num,0)+1
        count=len(p)
        left=0
        for right in range(len(s)):
            if s[right] in dict1:
                if dict1[s[right]]>0:
                    count-=1
                dict1[s[right]]-=1
            if right-left+1>len(p):
                if s[left] in dict1:
                    if dict1[s[left]]>=0:
                        count+=1
                    dict1[s[left]]+=1               
                left+=1
            if count==0:
                arr.append(left)
        return arr
