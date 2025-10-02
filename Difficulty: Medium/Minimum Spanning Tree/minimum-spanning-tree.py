class Solution:
    def spanningTree(self, V, edges):
        # code here
        vis=[0]*V
        
        adj=[[] for _ in range(V)]
        
        for u,v , wt in edges:
            adj[u].append([v,wt])
            adj[v].append([u,wt])
        
        import heapq
        min_heap=[]
        
        heapq.heappush(min_heap,[0,0])  #wt, node
        sum=0
        
        while min_heap:
            
            wt,node= heapq.heappop(min_heap)
            
            if vis[node]==1:
                continue
            vis[node]=1
            sum+=wt
            
            for adjNode, adjWt in adj[node]:
                if vis[adjNode]==0:
                    heapq.heappush(min_heap,[adjWt,adjNode])
        
        return sum
        