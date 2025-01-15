# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        pre=0
        res=0
        mp={}
        
        for i in range(len(arr)):
            pre+=arr[i]
            
            if pre==k:
                res=i+1
            
            
            elif pre-k in mp:
                res=max(res,i-mp[pre-k])
            
            if pre not in mp:
                mp[pre]=i
                
                
        return res
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends