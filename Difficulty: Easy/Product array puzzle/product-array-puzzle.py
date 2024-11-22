#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        i=0
        res=[]
        while(i<len(arr)):
            prod=1
            for j in range(len(arr)):
                if j!=i:
                    prod*=arr[j]
            res.append(prod)
            i+=1
        return res
                    
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends