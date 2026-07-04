from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph1=[[]for _ in range(len(graph))]
        indegree=[0]*len(graph)
        for i in range(len(graph)):
            for neighbour in graph[i]:
                graph1[neighbour].append(i)
                indegree[i]+=1
        queue=deque()
        topo=[]
        for i in  range(len(graph)):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            x=queue.popleft()
            topo.append(x)
            for  neighbour in graph1[x]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        return sorted(topo)
        


        