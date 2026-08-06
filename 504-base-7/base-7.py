class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        str1=""
        flag=1
        if num<0:
            num=-num
            flag=-1
        while num>0:
            str1=str(num%7)+str1
            num=num//7
        if flag==-1:
            return "-"+str1
        return str1

        