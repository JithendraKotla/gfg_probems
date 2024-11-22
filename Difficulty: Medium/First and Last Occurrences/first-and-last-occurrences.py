#User function Template for python3
    

class Solution:
    def find(self, arr, x):
        
        # code here
        res=[]
        j=0
        for i in arr:
        
            
            if i==x:
                res.append(j)
            j+=1
        if len(res)==0:
            return [-1,-1]
        elif len(res)==1:
            return [res[0],res[0]]
            
        return [res[0],res[-1]]
                


#{ 
 # Driver Code Starts
t = int(input())  # Number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array for each test case
    x = int(input())  # Element to search for
    ob = Solution()
    ans = ob.find(arr, x)  # Call the find function in the Solution class
    print(*ans)  # Print the result as space-separated values
    print("~")

# } Driver Code Ends