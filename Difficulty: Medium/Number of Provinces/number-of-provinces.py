#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        from collections import deque
        adjL=[[] for _ in range(V)]
        
        for i in range(V):
            for j in range(V):
                if adj[i][j]==1 and i!=j:
                    adjL[i].append(j)
                    adjL[j].append(i)
        vis=[0]*V
        
        
        
        
        def bfs(node):
            q=deque()
            q.append(node)
            vis[node]=1
            
            while q:
                n=q.popleft()
                
                for nei in adjL[n]:
                    if vis[nei]==0:
                        q.append(nei)
                        vis[nei]=1
        cnt=0
        for i in range(V):
            if vis[i]==0:
                bfs(i)
                cnt+=1
        return cnt
                    
            
        