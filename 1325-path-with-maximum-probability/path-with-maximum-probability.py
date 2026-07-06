import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph=[[]for _ in range(n)]
        for i in range(len(edges)):
            u,v=edges[i]
            p=succProb[i]
            graph[u].append((v,p))
            graph[v].append((u,p))
        prob=[0]*n
        prob[start_node]=1
        heap=[]
        heapq.heappush(heap,(-(prob[start_node]),start_node))
        while heap:
            current_prob,node=heapq.heappop(heap)
            if -(current_prob)<prob[node]:
                continue
            for neighbour,p in graph[node]:
                new_prob=(-current_prob)*p
                if new_prob>prob[neighbour]:
                    prob[neighbour]=new_prob
                    heapq.heappush(heap,(-new_prob,neighbour))
        return prob[end_node]





        
        