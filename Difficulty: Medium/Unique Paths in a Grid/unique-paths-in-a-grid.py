class Solution:
    def uniquePaths(self, grid):
        # code here 
        n=len(grid)
        m=len(grid[0])
        
        def f(i,j):
            if grid[i][j] == 1:   # obstacle check (if needed)
                return 0
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            left=f(i,j-1)
            up=f(i-1,j)
            
            dp[i][j]=left+up
            return dp[i][j]
        
        dp=[[-1 for _ in range(m)] for _ in  range(n)]
        
        return f(n-1,m-1)