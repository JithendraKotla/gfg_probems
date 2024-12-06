#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        hindex=0
        citations=sorted(citations,reverse=True)
        for i in range(len(citations)):
            if citations[i]>=i+1:
                hindex=i+1
        return hindex
        
                
            


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends