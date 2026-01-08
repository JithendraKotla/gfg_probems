#User function Template for python3
class Solution:
	def minDifference(self, nums):
		# code here
		n = len(nums)

        def f(ind, target, dp):
            if target == 0:
                return True
            if ind == 0:
                return nums[ind] == target
            if dp[ind][target] != -1:
                return dp[ind][target]

            nottake = f(ind - 1, target, dp)
            take = False
            if target >= nums[ind]:
                take = f(ind - 1, target - nums[ind], dp)

            dp[ind][target] = take or nottake
            return dp[ind][target]

        totsum = sum(nums)
        mini = float("inf")

        dp = [[-1 for _ in range(totsum + 1)] for _ in range(n)]
        for s1 in range(totsum // 2 + 1):
            if f(n - 1, s1, dp):
                s2 = totsum - s1
                mini = min(mini, abs(s2 - s1))

        return mini