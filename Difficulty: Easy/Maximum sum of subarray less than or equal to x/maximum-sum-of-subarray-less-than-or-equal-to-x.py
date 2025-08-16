
class Solution:
    def findMaxSubarraySum(self, arr, x):
        # Your code goes here
        l=0
        r=0
        n=len(arr)
        maxi=0
        maxsum=0
        
        while r<n:
            maxsum+=arr[r]
            
            while maxsum>x and l<=r:
                maxsum=maxsum-arr[l]
                l+=1
                
            maxi=max(maxi,maxsum)
            r+=1
        return maxi