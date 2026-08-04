class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        collection=0
        count5=0
        count10=0
        count20=0
        for bill in bills:
            if bill==5:
                count5+=1
            elif bill==10:
                count10+=1
                count5-=1
            elif bill==20:
                if count10>0:
                    count10-=1
                    count5-=1
                else:
                    count5-=3
                count20+=1
            if count5<0 or count10<0:
                return False
        return True

            
        