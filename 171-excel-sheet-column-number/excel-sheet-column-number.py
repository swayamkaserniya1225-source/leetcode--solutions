class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        x=len(columnTitle)-1
        current=0
        for num in columnTitle:
            current+=((ord(num)-ord("A"))+1)*(26**x)
            x-=1
        return current

