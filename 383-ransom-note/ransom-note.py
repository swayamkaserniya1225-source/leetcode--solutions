class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1={}
        for num in ransomNote:
            dict1[num]=dict1.get(num,0)+1
        for num1 in magazine:
            if num1 in dict1:
                if dict1[num1]>0:
                    dict1[num1]-=1
        return all(value==0 for value in dict1.values())
