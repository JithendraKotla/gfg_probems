class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
	    from collections import deque
		#Code here
		n=len(grid)
		m=len(grid[0])
		
		
		vis=[[0 for _ in range(m)] for _ in range(n)]
		
		dist=[[0 for _ in range(m)] for _ in range(n)]
		
		
		q=deque()
		
		for i in range(n):
		    for j in range(m):
		        if grid[i][j]==1:
		            q.append((i,j,0))
		            vis[i][j]=1
		        else:
		            vis[i][j]=0
		while q:
		    len_q=len(q)
		    for _ in range(len_q):
		        row,col,step=q.popleft()
		        dist[row][col]=step
		        for r,c in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
		            if 0<=r<n and 0<=c<m and vis[r][c]==0:
		                vis[r][c]=1
		                q.append((r,c,step+1))
		return dist
		                
		    