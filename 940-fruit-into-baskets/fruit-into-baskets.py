class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count={}
        left=0
        max1=0
        for  right in range (len(fruits)):
            if fruits[right] in count:
                count[fruits[right]]+=1
            elif fruits[right] not in count: 
                if len(count)==2:
                    total=0
                    for value in count.values():
                        total+=value
                    max1=max(total,max1)
                    while len(count)!=1:
                        count[fruits[left]]-=1
                        if count[fruits[left]]==0:
                            del count[fruits[left]]
                        left+=1
                count[fruits[right]]=1
        max1=max(max1,sum(count.values()))
        return max1




            




            
        