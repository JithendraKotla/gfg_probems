from collections import deque

class Solution:
    def findOrder(self, N, prerequisites):
        adj = [[] for _ in range(N)]
        indegree = [0] * N

        # Build graph + indegree
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        q = deque()
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # Return topo order if valid, else empty
        return topo if len(topo) == N else []
