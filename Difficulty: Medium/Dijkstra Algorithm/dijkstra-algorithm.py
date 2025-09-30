class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        dist=[float("inf")]*V
        dist[src]=0
        
        adj=[[] for _ in range(V)]
        
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w]) 
                
        
        
        
        min_heap=[]
        
        import heapq
        
        heapq.heappush(min_heap,(0,src))
        
        while min_heap:
            dis,node=heapq.heappop(min_heap)
            
            if dis>dist[node]:
                continue
            
            for nei in adj[node]:
                adjNode=nei[0]
                edW=nei[1]
                
                if edW+ dis  < dist[adjNode]:
                    dist[adjNode]=edW+dis
                    
                    heapq.heappush(min_heap,(dis+edW,adjNode))
                    
                 
                    
        return dist
            
                