class Solution:
    def countPartitions(self, arr, diff):
        # code here
        
        n=len(arr)
        
        def f(ind,target):
            MOD = 10**9 + 7
            if ind == 0:
                if target == 0 and arr[0] == 0:
                    return 2
                if target == 0 or arr[0] == target:
                    return 1
                return 0
            if dp[ind][target]!=-1:
                return dp[ind][target]
            take =0
            
            if target >=arr[ind]:
                take = f(ind - 1, target - arr[ind])
            nottake = f(ind - 1, target)

            dp[ind][target] = (take + nottake) % MOD
            return dp[ind][target]
        
        summa= sum(arr)
        target = (summa-diff)//2
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]  
        if (summa-diff)%2 !=0 or summa-diff<0:
            return 0
        else:
            return f(n-1,target)

        
            
        
