class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count={}
        for num  in s1:
            count[num]=count.get(num,0)+1
        left=0
        for right in range(len(s2)):
            if s2[right] in count:
                count[s2[right]]-=1
            if right-left+1>len(s1):
                if s2[left]in count:
                    count[s2[left]]+=1
                left+=1
            flag=True
            for value in count.values():
                if value!=0:
                    flag=False
                    break
            if flag==True:
                return True
        return False
                