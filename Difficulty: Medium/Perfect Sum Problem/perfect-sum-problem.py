# User function Template for python3
class Solution:
    # Recursive helper function
    def countSubsets(self, i, currentSum, target, arr, memo):
        n = len(arr)
    
        # Base case: If we've processed all elements
        if i == n:
            return 1 if currentSum == target else 0
    
        # Check if result is already computed
        if memo[i][currentSum] != -1:
            return memo[i][currentSum]
    
        # Case 1: Exclude the current element
        exclude = self.countSubsets(i + 1, currentSum, target, arr, memo)
    
        # Case 2: Include the current element
        include = 0
        if currentSum + arr[i] <= target:
            include = self.countSubsets(i + 1, currentSum + arr[i], target, arr, memo)
    
        # Store result in memoization table and return it
        memo[i][currentSum] = include + exclude
        return memo[i][currentSum]
    
    # Main function
    def perfectSum(self, arr, target):
        n = len(arr)
        
        # Initialize a 2D memoization table with -1
        memo = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
    
        return self.countSubsets(0, 0, target, arr, memo)
