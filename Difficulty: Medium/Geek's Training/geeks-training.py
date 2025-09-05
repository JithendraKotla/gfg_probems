#User function Template for python3

class Solution:
    def maximumPoints(self, arr):
        # Code here
        def f(day,last,dp,arr):
            if dp[day][last]!=-1:
                return dp[day][last]
            
            if day==0:
                maxi=0
                for i in range(3):
                    if i!=last:
                        maxi=max(maxi,arr[0][i])
                dp[day][last]=maxi
                return dp[day][last]
            
            
            maxi=0
            
            for i in range(3):
                if i!=last:
                    activity=arr[day][i]+f(day-1,i,dp,arr)
                    maxi=max(maxi,activity)
            
            dp[day][last]=maxi
            return dp[day][last]
        n=len(arr)
            
        dp=[[-1 for j in range(4)] for i in range(n)]
        day=n-1
        last=3
        
        return f(day,last,dp,arr)
        
        
        
        
        
        
        
        
        
        
        
        
        
        dp=[-1]*len(arr)