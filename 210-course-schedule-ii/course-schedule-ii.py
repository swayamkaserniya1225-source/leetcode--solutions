from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: 
        graph=[[]for _ in range(numCourses)]
        indegree=[0]*numCourses
        for  course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1
        queue=deque()
        for  i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        topo=[]
        while queue:
            x=queue.popleft()
            topo.append(x)
            for neighbour in graph[x]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        if len(topo)==numCourses:
            return topo
        return []
        