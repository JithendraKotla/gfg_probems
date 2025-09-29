#User function Template for python3

class Solution:
    def isPossible(self,N,P,prerequisites):
        #code here
        from collections import deque
        adj=[[] for _ in range(N)]
        
        for u,v in prerequisites:
            adj[v].append(u)
        
        indegree=[0]*N
        
        q=deque()
        
        for i in range(N):
            for j in adj[i]:
                indegree[j]+=1
        topo=[]
        
        for i in range(N):
            if indegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            topo.append(node)
            
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return len(topo)==N
                    