#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        dist=[10**8 for _ in range(V)]
        dist[src]=0
        
        for _ in range(V):
        
            for u,v, wt in edges:
                if dist[u] !=10**8  and  dist[u]+wt < dist[v]:
                    dist[v]=dist[u]+wt
                    
        for u,v , wt in edges:
            if dist[u] != 10**8 and  dist[u]+wt < dist[v]:
                return [-1]
        
        return dist
        
            