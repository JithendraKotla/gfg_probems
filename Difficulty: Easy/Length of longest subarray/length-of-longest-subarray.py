#User function Template for python3
class Solution:
    def longestSubarray(self, arr):
        #write code here
        l=0
        r=0
        maxi=0
        n=len(arr)
        
        while r<n:
            if arr[r]<0:
                l=r+1
            else:
                maxi=max(r-l+1,maxi)
            r+=1
        return maxi
                
    
    
    