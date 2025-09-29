
class Solution:
    def shortestPath(self, adj, src):
        # code here
        from collections import deque
        
        q=deque()
        
        dist=[float("inf") for _ in range(len(adj))]
        dist[src]=0
        
        q.append(src)
        
        
        while q:
            node=q.popleft()
            
            for nei in adj[node]:
                if 1+dist[node]<dist[nei]:
                    dist[nei]=1+dist[node]
                    q.append(nei)
        for i in range(len(dist)):
            if dist[i] == float("inf"):
                dist[i] = -1
        return dist
        
        
