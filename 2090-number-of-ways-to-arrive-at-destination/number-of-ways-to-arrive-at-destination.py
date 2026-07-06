import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph=[[]for _ in range(n)]
        for u,v,w  in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        dist=[float("inf")]*n
        dist[0]=0
        ways=[0]*n
        heap=[]
        heapq.heappush(heap,(0,0))
        ways[0]=1
        while heap:
            current_distance,node=heapq.heappop(heap)
            if current_distance>dist[node]:
                continue
            for  neighbour,weight in graph[node]:
                new_distance=current_distance+weight
                if new_distance<dist[neighbour]:
                    dist[neighbour]=new_distance
                    ways[neighbour]=ways[node]
                    heapq.heappush(heap,(new_distance,neighbour))
                elif new_distance==dist[neighbour]:
                    ways[neighbour]+=ways[node]
                    
        return ways[n-1]%(10**9+7)