# User function Template for python3

class Solution:
    def graphColoring(self, V, edges, m):
        # code here
        def isSafe(node,color,graph,N,col):
            for k in range(N):
                if node!=k and graph[node][k]==1 and color[k]==col:
                    return False
            return True
        
        def solve(node,color,m,N,graph):
            if node==N:
                return True
            for i in range(1,m+1):
                if isSafe(node,color,graph,N,i):
                    color[node]=i
                    if solve(node+1,color,m,N,graph):
                        return True
                    color[node]=0
            return False
                    
        graph=[[0]*V for _ in range(V)]
        
        for u,v in edges:
            graph[u][v]=1
            graph[v][u]=1
        
        color=[0]*V
        
        return solve(0, color, m, V, graph)
        