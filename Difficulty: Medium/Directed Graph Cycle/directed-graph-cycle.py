
class Solution:
    def isCycle(self, V, edges):
        # code here
        adj=[[] for _ in range(V)]
        
        for u,v in edges:
            adj[u].append(v)
            
        indegree=[0]*V
        
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        
        topo=[]
        
        q=deque()
        
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            topo.append(node)
            
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return len(topo)!=V