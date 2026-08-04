class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        arr1=[]
        left=0
        dict1={}
        count=0
        for right in range(len(s)):
            if s[right] not  in  dict1:
                dict1[s[right]]=[right,right]
            else:
                dict1[s[right]][1]=right
        x=list(dict1.values())
        max_val=x[0][1]
        start=[0][0]
        for i in range(1,len(x)):
            if max_val<x[i][0]:
                arr1.append(max_val-start+1)
                start=x[i][0]
                max_val=x[i][1]
            else:
                max_val=max(max_val,x[i][1])
        arr1.append(max_val-start+1)
        return arr1












        