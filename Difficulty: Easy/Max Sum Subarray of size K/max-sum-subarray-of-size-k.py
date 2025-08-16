class Solution:
    def maximumSumSubarray (self,arr,k):
        # code here 
        maxi=0
        l=0
        r=0
        n=len(arr)
        maxsum=0
        
        while r<n:
            maxsum+=arr[r]
            while r-l+1>k:
                maxsum-=arr[l]
                l+=1
                
            r+=1
            maxi=max(maxsum,maxi)
        return maxi
        
            
            
            
            