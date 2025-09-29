#User function Template for python3

from typing import List


class Solution:
    def topoSort(self,node,adj,vis,st):
        vis[node]=1
        for v,wt in adj[node]:
            if not vis[v]:
                self.topoSort(v,adj,vis,st)
        st.append(node)

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(V)]
        
        for u, v, wt in edges:
            adj[u].append((v,wt))
        
        
        vis=[0]*V
        
        st=[]
        
        for i in range(V):
            if vis[i]==0:
                self.topoSort(i,adj,vis,st)
        
        dist=[10**9]*V
        dist[0]=0
        
        while st:
            node=st.pop()
            
            for nei in adj[node]:
                v=nei[0]
                wt=nei[1]
                
                if wt+dist[node]<dist[v]:
                    dist[v]=wt+dist[node]
                    
        for i in range(V):
            if dist[i]==10**9:
                dist[i]=-1
        return dist
            
        pass
