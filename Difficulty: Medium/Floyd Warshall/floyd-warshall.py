class Solution:
    def floydWarshall(self, dist):
        n = len(matrix)
        V = len(dist)

    # Add all vertices one by one to
    # the set of intermediate vertices.
        for k in range(V):
    
            # Pick all vertices as source one by one
            for i in range(V):
    
                # Pick all vertices as destination
                # for the above picked source
                for j in range(V):
                    #shortest path from
                    #i to j 
                    if(dist[i][k] != 100000000 and dist[k][j]!= 100000000):
                        dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j]);
