import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[]for i in range(n+1)]
        dist=[float("inf")]*(n+1)
        dist[k]=0
        for u,v,w in times:
            graph[u].append((v,w))
        heap=[]
        heapq.heappush(heap,(0,k))
        while heap:
            current_distance,node=heapq.heappop(heap)
            if current_distance>dist[node]:
                continue
            for neighbour,weight in graph[node]:
                new_distance=current_distance+weight
                if new_distance<dist[neighbour]:
                    dist[neighbour]=new_distance
                    heapq.heappush(heap,(new_distance,neighbour))
        if max(dist[1:])==float("inf"):
            return -1
        return max(dist[1:])
        