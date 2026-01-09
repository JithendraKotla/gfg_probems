#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
		# code here
		n=len(arr)
		def f(ind,target):
		    if ind == 0:
                if target == 0 and arr[0] == 0:
                    return 2
                if target == 0 or arr[0] == target:
                    return 1
                return 0
		    if dp[ind][target]!=-1:
		        return dp[ind][target]
		    take =0
		    if arr[ind]<=target:
		        take = f(ind-1,target- arr[ind])
		    
		    nottake = f(ind-1,target)
		    
		    dp[ind][target]= take + nottake
		    
		    return dp[ind][target]
	    
	    dp=[[-1 for _ in range(target+1)] for _ in range(n)]
	    
	    return f(n-1,target)