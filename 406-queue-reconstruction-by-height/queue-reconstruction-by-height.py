
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # people.sort(reverse=True)
        people.sort(key=lambda x:(-x[0],x[1]))
        # return people
        start=0
        queue=[]
        for i in range(len(people)):
            queue.insert(people[i][1],people[i])
        return queue



         

        



        