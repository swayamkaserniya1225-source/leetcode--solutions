class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        arr1=[]
        start=0
        end=0
        dict1={}
        for i,ch  in enumerate(s):
            dict1[ch]=i
        for i,ch in  enumerate(s):
            end=max(end,dict1[ch])
            if i==end:
                arr1.append(end-start+1)
                start=i+1
        return arr1













        