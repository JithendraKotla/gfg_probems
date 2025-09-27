class Solution:
    # Function to return connected components of the graph
    def getComponents(self, V, edges):
        # code here
        def dfs(node, adjList, vis, comp):
            vis[node] = 1
            comp.append(node)
            for nei in adjList[node]:
                if not vis[nei]:
                    dfs(nei, adjList, vis, comp)

        # Build adjacency list (efficient)
        adjList = [[] for _ in range(V)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        vis = [0] * V
        components = []

        for i in range(V):
            if vis[i] == 0:
                comp = []
                dfs(i, adjList, vis, comp)
                components.append(comp)

        return components
        
        
        