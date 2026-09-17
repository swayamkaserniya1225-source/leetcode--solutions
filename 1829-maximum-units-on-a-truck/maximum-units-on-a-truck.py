class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        count=0
        for num,val in boxTypes:
            if truckSize>num:
                count+=(num*val)
                truckSize-=num
            else:
                count+=(truckSize*val)
                return count
        return count
            

            
        