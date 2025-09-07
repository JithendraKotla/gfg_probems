class Solution:
    def isSubsetSum (self, arr, sum):
        n=len(arr)
        # code here 
        def f(ind,target):
            if target==0:
                return True
            
            if ind==0:
                return arr[ind]==target
            if dp[ind][target] != -1:
                return dp[ind][target]
                
            nottaken=f(ind-1,target)
            
            taken=False
            
            if arr[ind]<=target:
                taken = f(ind - 1, target - arr[ind])
                
            dp[ind][target] = nottaken or taken
            return dp[ind][target]
        dp=[[-1 for _ in range(sum+1)] for _ in range(n)]
        ind=n-1
        
        return f(ind,sum)

            