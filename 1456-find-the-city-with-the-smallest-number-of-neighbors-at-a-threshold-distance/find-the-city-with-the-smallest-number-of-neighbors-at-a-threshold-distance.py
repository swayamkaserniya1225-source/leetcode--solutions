import  heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def helper(sources):
            dist=[float("inf")]*n
            dist[sources]=0
            heap=[]
            heapq.heappush(heap,(0,sources))
            while heap:
                current_distance,node=heapq.heappop(heap)
                if current_distance>dist[node]:
                    continue
                for  neighbour,weight in graph[node]:
                    new_distance=current_distance+weight
                    if new_distance<dist[neighbour]:
                        dist[neighbour]=new_distance
                        heapq.heappush(heap,(new_distance,neighbour))
            count=0
            for num in dist:
                if num<=distanceThreshold:
                    count+=1
            return count-1
        graph=[[]for _ in range(n)]
        for u,v,w  in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        min_count=float("inf")
        answer=-1
        for sources in range(len(graph)):
            count=helper(sources)
            if count<=min_count:
                min_count=count
                answer=sources
        return answer
       
        
        
                    
                
                




            


        