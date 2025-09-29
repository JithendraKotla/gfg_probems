class Solution:
    def topoSort(self, V, edges):
        # Code here
        from collections import deque
        adj=[[] for _ in range(V)]
        indegree=[0]*V
        
        for u,v in edges:
            adj[u].append(v)
        
        for i in  range(V):
            for j in adj[i]:
                indegree[j]+=1
        
        q=deque()
        
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        topo=[]
        
        while q:
            node=q.popleft()
            topo.append(node)
            
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return topo
            
                