class Solution:
	def isCycle(self, V, edges):
		#Code here
		from collections import deque
		def detectCycle(node,adjList,vis):
		    q=deque()
		    q.append((node,-1))
		    vis[node] = 1
		    
		    while q:
		        len_q=len(q)
		        
		        for _ in range(len_q):
		            child,parent=q.popleft()
		            for nei in adjList[child]:
		                if (vis[nei]==0):
		                    vis[nei]=1
		                    q.append((nei,child))
		                elif parent!=nei:
		                    return True
		    return False
		vis=[0]*V
		adjList=[[] for _ in range(V)]
		
		for u,v in edges:
		    adjList[u].append(v)
		    adjList[v].append(u)
		 
		for i in range(V):
		   if (vis[i]==0):
		       if detectCycle(i,adjList,vis):
		           return True
		return False
		         
		            