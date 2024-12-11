class Solution:
    def mergeArrays(self, a, b):
        # code here
        al=0
        for i in a:
            al+=1
        bl=0
        for i in b:
            bl+=1
        
        t=al+bl
        
        for i in range(len(b)):
            a.append(b[i])
        
        
        a.sort()
       
        
        j=0
        for i in range(al,t):
            b[j]=a[i]
            j+=1
            
        
        for i in range(bl):
            a.pop()

#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends