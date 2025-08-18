#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        
        i=0
        j=0
        
        cnt=0
        maxcnt=0
        n=len(arr)
        
        while i<n:
            if arr[i]<=dep[j]:
                cnt+=1
                i+=1
            else:
                cnt-=1
                j+=1
            maxcnt=max(cnt,maxcnt)
        return maxcnt