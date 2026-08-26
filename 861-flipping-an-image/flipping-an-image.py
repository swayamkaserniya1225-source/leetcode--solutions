class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            left=0
            right=len(image)-1
            while left<right:
                if image[i][left]==0:
                    image[i][left]=1
                else:
                    image[i][left]=0
                if image[i][right]==0:
                    image[i][right]=1
                else:
                    image[i][right]=0
                image[i][left],image[i][right]=image[i][right],image[i][left]
                left+=1
                right-=1
            if left==right:
                image[i][left]=1-image[i][left]
        return image

                