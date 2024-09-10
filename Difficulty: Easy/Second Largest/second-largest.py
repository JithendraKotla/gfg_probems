#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        arr=set(arr)
        arr=list(arr)
        if len(arr)<2:
            return -1
        
        else:
            arr.sort()
            j=len(arr)-2
            return arr[j]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends