from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        return len(topo)==numCourses

        