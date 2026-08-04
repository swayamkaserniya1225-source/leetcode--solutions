
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        queue=[]
        for per in people:
            queue.insert(per[1],per)
        return queue



         

        



        