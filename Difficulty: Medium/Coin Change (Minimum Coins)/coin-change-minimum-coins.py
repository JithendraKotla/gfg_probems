class Solution:
	def minCoins(self, arr, sum):
		# code here
	   
	   n=len(arr)
       INF = 10**9

       def f(ind, target):
            if ind == 0:
                if target % arr[ind] == 0:
                   return target // arr[ind]
                else:
                    return INF

            if dp[ind][target] is not None:
                return dp[ind][target]

            not_take = f(ind - 1, target)

            take = INF
            if target >= arr[ind]:
                take = 1 + f(ind, target - arr[ind])

            dp[ind][target] = min(take, not_take)
            return dp[ind][target]

       dp = [[None for _ in range(sum + 1)] for _ in range(n)]
       ans = f(n - 1, sum)
       return -1 if ans >= INF else ans 