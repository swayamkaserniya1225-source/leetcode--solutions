class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        count=1
        points.sort(key=lambda x:(x[0],x[1]))
        x=points[0][1]
        for right in range(1,len(points)):
            if points[right][0]>x:
                count+=1
                x=points[right][1]
            else:
                x=min(points[right][1],x)
        return count

        