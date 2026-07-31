class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hash={}
        left=0
        for num in s1:
            hash[num]=hash.get(num,0)+1
        for right in  range(len(s2)):
            if s2[right] in hash:
                hash[s2[right]]-=1
            if right-left+1>len(s1):
                if s2[left] in hash:
                    hash[s2[left]]+=1
                left+=1
            flag=True
            for value in hash.values():
                if value!=0:
                    flag=False
                    break
            if flag==True:
                return True
        return False
                


