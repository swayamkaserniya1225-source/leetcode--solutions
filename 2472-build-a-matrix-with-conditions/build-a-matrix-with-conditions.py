class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        from collections import deque
        def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
            graph=[[]for _ in range(numCourses)]
            indegree=[0]*numCourses
            for  course,pre in prerequisites:
                graph[course].append(pre)
                indegree[pre]+=1
            queue=deque()
            for  i in range(1,numCourses):
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
            if len(topo) != numCourses - 1:
                return []
            return topo
        rowdegree=canFinish(k+1,rowConditions)
        columndegree=canFinish(k+1,colConditions)
        if not rowdegree or not columndegree:
            return []
        row_position={}
        for i,j in enumerate(rowdegree):
            row_position[j]=i
        column_position={}
        for i,j in enumerate(columndegree):
            column_position[j]=i
        matrix=[[0]*k for i in range(k)]
        for num in range(1,k+1):
            matrix[row_position[num]][column_position[num]] = num
        return matrix
        



            