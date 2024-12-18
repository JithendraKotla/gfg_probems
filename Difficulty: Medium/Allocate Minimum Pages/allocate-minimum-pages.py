class Solution:
    
    #Function to find minimum number of pages.
    
        
    def findPages(self, arr, k):
        #code here
        def check(arr,k,limitpage):
            pagesum=0
            cn=1
            for i in arr:
                if pagesum+i>limitpage:
                    cn+=1
                    pagesum=i
                else:
                    pagesum+=i
            return cn<=k
        if k > len(arr):
            return -1
        lo = max(arr)
        hi = sum(arr)
        res = -1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if check(arr, k, mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
                
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends