class Solution:

    def aggressiveCows(self, stalls, k):
        # your code here
        def possible(stalls,k,mid):
            cnt=1
            n=len(stalls)
            last=stalls[0]
            for i in range(1,n):
                if stalls[i]-last>=mid:
                    cnt+=1
                    last=stalls[i]
                if cnt>=k:
                    return True
            return False
        n=len(stalls)
        stalls.sort()
        low=1
        high=stalls[n-1]-stalls[0]
        while low<=high:
            mid=(low+high)//2
            if possible(stalls,k,mid):
                low=mid+1
            else:
                high=mid-1
        return high
                
